#include <UTFT.h> 

#ifdef __arm__
// should use uinstd.h to define sbrk but Due causes a conflict
extern "C" char* sbrk(int incr);
#else  // __ARM__
extern char *__brkval;
#endif  // __arm__

int freeMemory() {
  char top;
#ifdef __arm__
  return &top - reinterpret_cast<char*>(sbrk(0));
#elif defined(CORE_TEENSY) || (ARDUINO > 103 && ARDUINO != 151)
  return &top - __brkval;
#else  // __arm__
  return __brkval ? &top - __brkval : &top - __malloc_heap_start;
#endif  // __arm__
}

// 320x240

UTFT myGLCD(ILI9341_16,38,39,40,41);

unsigned char animacion_actual = 0;

const unsigned char enfadado[] PROGMEM = { 96, 136, 0, 0, 1, 0, 0, 1, 3, 1, 1, 1, 3, 3, 4, 3, 4, 1, 1, 2, 3, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 4, 8, 8, 17, 2, 0, 3, 11, 2, 0, 9, 18, 14, 15, 26, 11, 13, 4, 4, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 4, 12, 31, 25, 35, 9, 10, 11, 19, 4, 1, 3, 7, 7, 255, 7, 8, 255, 7, 9, 255, 7, 10, 255, 7, 11, 255, 7, 12, 255, 7, 19, 255, 7, 20, 255, 7, 21, 255, 7, 22, 255, 7, 23, 255, 7, 24, 255, 8, 6, 255, 8, 7, 255, 8, 8, 255, 8, 9, 255, 8, 10, 255, 8, 11, 255, 8, 12, 255, 8, 13, 255, 8, 18, 255, 8, 19, 255, 8, 20, 255, 8, 21, 255, 8, 22, 255, 8, 23, 255, 8, 24, 255, 8, 25, 255, 9, 6, 255, 9, 7, 255, 9, 8, 255, 9, 9, 255, 9, 10, 255, 9, 11, 255, 9, 12, 255, 9, 13, 255, 9, 18, 255, 9, 19, 255, 9, 20, 255, 9, 21, 255, 9, 22, 255, 9, 23, 255, 9, 24, 255, 9, 25, 255, 10, 6, 255, 10, 7, 255, 10, 8, 255, 10, 9, 255, 10, 10, 255, 10, 11, 255, 10, 12, 255, 10, 13, 255, 10, 18, 255, 10, 19, 255, 10, 20, 255, 10, 21, 255, 10, 22, 255, 10, 23, 255, 10, 24, 255, 10, 25, 255, 11, 6, 255, 11, 7, 255, 11, 8, 255, 11, 9, 255, 11, 10, 255, 11, 11, 255, 11, 12, 255, 11, 13, 255, 11, 18, 255, 11, 19, 255, 11, 20, 255, 11, 21, 255, 11, 22, 255, 11, 23, 255, 11, 24, 255, 11, 25, 255, 12, 6, 255, 12, 7, 255, 12, 8, 255, 12, 9, 255, 12, 10, 255, 12, 11, 255, 12, 12, 255, 12, 13, 255, 12, 18, 255, 12, 19, 255, 12, 20, 255, 12, 21, 255, 12, 22, 255, 12, 23, 255, 12, 24, 255, 12, 25, 255, 13, 6, 255, 13, 7, 255, 13, 8, 255, 13, 9, 255, 13, 10, 255, 13, 11, 255, 13, 12, 255, 13, 13, 255, 13, 18, 255, 13, 19, 255, 13, 20, 255, 13, 21, 255, 13, 22, 255, 13, 23, 255, 13, 24, 255, 13, 25, 255, 14, 6, 255, 14, 7, 255, 14, 8, 255, 14, 9, 255, 14, 10, 255, 14, 11, 255, 14, 12, 255, 14, 13, 255, 14, 18, 255, 14, 19, 255, 14, 20, 255, 14, 21, 255, 14, 22, 255, 14, 23, 255, 14, 24, 255, 14, 25, 255, 15, 7, 255, 15, 8, 255, 15, 9, 255, 15, 10, 255, 15, 11, 255, 15, 12, 255, 15, 19, 255, 15, 20, 255, 15, 21, 255, 15, 22, 255, 15, 23, 255, 15, 24, 255, 15, 18, 255, 7, 18, 255, 7, 13, 255, 7, 25, 255, 15, 13, 255, 15, 25, 255, 7, 6, 255, 15, 6, 255, 11, 14, 255, 11, 17, 255, 12, 17, 255, 10, 14, 255, 10, 17, 255, 12, 14, 255, 9, 17, 255, 11, 26, 255, 13, 14, 255, 13, 17, 255, 9, 14, 255, 10, 26, 255, 12, 26, 255, 9, 26, 255, 10, 5, 255, 11, 5, 255, 12, 5, 255, 9, 5, 255, 13, 26, 255, 8, 14, 255, 13, 5, 255, 8, 17, 255, 8, 26, 255, 14, 17, 255, 8, 5, 255, 14, 14, 255, 14, 26, 255, 14, 26, 0, 6, 10, 255, 6, 21, 255, 6, 22, 255, 6, 9, 255, 8, 5, 0, 14, 14, 0, 14, 17, 0, 6, 8, 255, 6, 11, 255, 6, 20, 255, 6, 23, 255, 8, 14, 0, 8, 17, 0, 8, 26, 0, 13, 5, 0, 6, 12, 255, 6, 19, 255, 9, 5, 0, 10, 5, 0, 12, 5, 0, 13, 14, 0, 13, 17, 0, 13, 26, 0, 6, 7, 255, 6, 24, 255, 9, 14, 0, 9, 17, 0, 9, 26, 0, 10, 14, 0, 10, 17, 0, 10, 26, 0, 11, 5, 0, 11, 17, 0, 11, 26, 0, 12, 14, 0, 12, 17, 0, 12, 26, 0, 15, 6, 0, 15, 13, 0, 15, 25, 0, 11, 14, 0, 15, 18, 0, 5, 10, 255, 5, 21, 255, 5, 22, 255, 5, 8, 255, 5, 9, 255, 5, 11, 255, 5, 20, 255, 5, 23, 255, 14, 6, 0, 14, 13, 0, 14, 25, 0, 15, 7, 0, 15, 12, 0, 15, 24, 0, 14, 18, 0, 15, 19, 0, 5, 8, 0, 5, 9, 0, 5, 10, 0, 5, 11, 0, 5, 20, 0, 5, 21, 0, 5, 22, 0, 5, 23, 0, 13, 6, 0, 6, 7, 0, 6, 8, 0, 6, 10, 0, 6, 11, 0, 6, 12, 0, 6, 19, 0, 6, 20, 0, 6, 21, 0, 6, 23, 0, 6, 24, 0, 7, 6, 0, 7, 13, 0, 7, 18, 0, 7, 25, 0, 13, 6, 255, 14, 13, 255, 14, 18, 255, 15, 19, 255, 6, 9, 0, 6, 22, 0, 7, 7, 0, 7, 10, 0, 7, 11, 0, 7, 12, 0, 7, 19, 0, 7, 20, 0, 7, 21, 0, 7, 24, 0, 8, 6, 0, 8, 13, 0, 8, 18, 0, 15, 12, 255, 7, 8, 0, 7, 9, 0, 7, 22, 0, 7, 23, 0, 8, 10, 0, 8, 11, 0, 8, 12, 0, 8, 19, 0, 8, 20, 0, 8, 21, 0, 8, 25, 0, 9, 13, 0, 9, 18, 0, 15, 7, 255, 15, 24, 255, 8, 7, 0, 8, 8, 0, 8, 9, 0, 8, 22, 0, 8, 23, 0, 8, 24, 0, 9, 6, 0, 9, 10, 0, 9, 11, 0, 9, 12, 0, 9, 19, 0, 9, 20, 0, 9, 21, 0, 9, 25, 0, 10, 13, 0, 10, 18, 0, 12, 14, 255, 12, 17, 255, 13, 14, 255, 13, 17, 255, 14, 6, 255, 14, 14, 255, 14, 17, 255, 14, 25, 255, 15, 13, 255, 15, 18, 255, 9, 7, 0, 9, 8, 0, 9, 9, 0, 9, 22, 0, 9, 23, 0, 9, 24, 0, 10, 11, 0, 10, 12, 0, 10, 19, 0, 10, 20, 0, 11, 18, 0, 10, 6, 0, 10, 9, 0, 10, 10, 0, 10, 21, 0, 10, 22, 0, 10, 25, 0, 11, 12, 0, 11, 13, 0, 11, 19, 0, 12, 14, 0, 12, 17, 0, 15, 14, 255, 15, 17, 255, 10, 7, 0, 10, 8, 0, 10, 23, 0, 10, 24, 0, 11, 11, 0, 11, 20, 0, 12, 13, 0, 12, 18, 0, 11, 21, 0, 11, 10, 0, 12, 19, 0, 12, 19, 255, 11, 10, 255, 11, 21, 255, 11, 11, 255, 11, 20, 255, 12, 13, 255, 12, 18, 255, 10, 7, 255, 10, 8, 255, 10, 9, 255, 10, 22, 255, 10, 23, 255, 10, 24, 255, 11, 12, 255, 11, 19, 255, 12, 14, 255, 12, 17, 255, 15, 14, 0, 15, 17, 0, 9, 7, 255, 9, 8, 255, 9, 9, 255, 9, 10, 255, 9, 21, 255, 9, 22, 255, 9, 23, 255, 9, 24, 255, 10, 6, 255, 10, 10, 255, 10, 11, 255, 10, 12, 255, 10, 13, 255, 10, 18, 255, 10, 19, 255, 10, 20, 255, 10, 21, 255, 10, 25, 255, 11, 13, 255, 11, 18, 255, 12, 14, 0, 12, 17, 0, 13, 14, 0, 13, 17, 0, 14, 6, 0, 14, 14, 0, 14, 17, 0, 14, 25, 0, 15, 7, 0, 15, 13, 0, 15, 18, 0, 8, 7, 255, 8, 8, 255, 8, 9, 255, 8, 10, 255, 8, 11, 255, 8, 12, 255, 8, 19, 255, 8, 20, 255, 8, 21, 255, 8, 22, 255, 8, 23, 255, 8, 24, 255, 9, 6, 255, 9, 11, 255, 9, 12, 255, 9, 13, 255, 9, 18, 255, 9, 19, 255, 9, 20, 255, 9, 25, 255, 13, 6, 0, 13, 25, 0, 15, 12, 0, 15, 19, 0, 15, 24, 0, 6, 8, 255, 6, 9, 255, 6, 10, 255, 6, 11, 255, 6, 20, 255, 6, 21, 255, 6, 22, 255, 6, 23, 255, 7, 7, 255, 7, 8, 255, 7, 9, 255, 7, 10, 255, 7, 11, 255, 7, 12, 255, 7, 19, 255, 7, 20, 255, 7, 21, 255, 7, 22, 255, 7, 23, 255, 7, 24, 255, 8, 13, 255, 8, 18, 255, 9, 6, 0, 10, 6, 0, 11, 6, 0, 12, 6, 0, 12, 25, 0, 14, 13, 0, 14, 18, 0, 15, 8, 0, 15, 9, 0, 15, 10, 0, 15, 11, 0, 15, 20, 0, 15, 23, 0, 6, 7, 255, 6, 12, 255, 6, 19, 255, 6, 24, 255, 10, 25, 0, 11, 25, 0, 13, 13, 0, 15, 21, 0, 15, 22, 0, 7, 13, 255, 7, 18, 255, 8, 25, 255, 9, 6, 255, 10, 6, 255, 10, 25, 255, 11, 6, 255, 11, 25, 255, 12, 25, 255, 13, 13, 255, 7, 25, 255, 8, 6, 255, 12, 6, 255, 13, 6, 255, 13, 25, 255, 14, 13, 255, 14, 18, 255, 15, 9, 255, 15, 10, 255, 15, 21, 255, 15, 22, 255, 6, 7, 0, 6, 8, 0, 6, 9, 0, 6, 10, 0, 6, 11, 0, 6, 12, 0, 6, 19, 0, 6, 20, 0, 6, 21, 0, 6, 22, 0, 6, 23, 0, 6, 24, 0, 7, 6, 255, 14, 6, 255, 14, 25, 255, 15, 8, 255, 15, 11, 255, 15, 20, 255, 15, 23, 255, 15, 7, 255, 15, 12, 255, 15, 19, 255, 15, 24, 255, 7, 6, 0, 7, 13, 0, 7, 18, 0, 7, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
const unsigned char corazon [] PROGMEM = { 94, 136, 0, 0, 1, 7, 25, 10, 30, 25, 50, 29, 16, 11, 12, 8, 12, 6, 0, 0, 3, 13, 10, 11, 11, 0, 8, 15, 17, 8, 0, 0, 2, 7, 2, 5, 0, 1, 2, 0, 0, 2, 3, 0, 8, 4, 6, 6, 0, 0, 0, 5, 4, 6, 4, 5, 3, 4, 7, 3, 6, 1, 0, 0, 0, 0, 8, 9, 7, 8, 6, 10, 2, 7, 19, 16, 25, 26, 23, 1, 11, 22, 1, 7, 17, 5, 3, 4, 1, 0, 0, 0, 0, 0, 0, 7, 7, 255, 7, 8, 255, 7, 9, 255, 7, 10, 255, 7, 11, 255, 7, 12, 255, 7, 19, 255, 7, 20, 255, 7, 21, 255, 7, 22, 255, 7, 23, 255, 7, 24, 255, 8, 6, 255, 8, 7, 255, 8, 8, 255, 8, 9, 255, 8, 10, 255, 8, 11, 255, 8, 12, 255, 8, 13, 255, 8, 18, 255, 8, 19, 255, 8, 20, 255, 8, 21, 255, 8, 22, 255, 8, 23, 255, 8, 24, 255, 8, 25, 255, 9, 6, 255, 9, 7, 255, 9, 8, 255, 9, 9, 255, 9, 10, 255, 9, 11, 255, 9, 12, 255, 9, 13, 255, 9, 18, 255, 9, 19, 255, 9, 20, 255, 9, 21, 255, 9, 22, 255, 9, 23, 255, 9, 24, 255, 9, 25, 255, 10, 6, 255, 10, 7, 255, 10, 8, 255, 10, 9, 255, 10, 10, 255, 10, 11, 255, 10, 12, 255, 10, 13, 255, 10, 18, 255, 10, 19, 255, 10, 20, 255, 10, 21, 255, 10, 22, 255, 10, 23, 255, 10, 24, 255, 10, 25, 255, 11, 6, 255, 11, 7, 255, 11, 8, 255, 11, 9, 255, 11, 10, 255, 11, 11, 255, 11, 12, 255, 11, 13, 255, 11, 18, 255, 11, 19, 255, 11, 20, 255, 11, 21, 255, 11, 22, 255, 11, 23, 255, 11, 24, 255, 11, 25, 255, 12, 6, 255, 12, 7, 255, 12, 8, 255, 12, 9, 255, 12, 10, 255, 12, 11, 255, 12, 12, 255, 12, 13, 255, 12, 18, 255, 12, 19, 255, 12, 20, 255, 12, 21, 255, 12, 22, 255, 12, 23, 255, 12, 24, 255, 12, 25, 255, 13, 6, 255, 13, 7, 255, 13, 8, 255, 13, 9, 255, 13, 10, 255, 13, 11, 255, 13, 12, 255, 13, 13, 255, 13, 18, 255, 13, 19, 255, 13, 20, 255, 13, 21, 255, 13, 22, 255, 13, 23, 255, 13, 24, 255, 13, 25, 255, 14, 6, 255, 14, 7, 255, 14, 8, 255, 14, 9, 255, 14, 10, 255, 14, 11, 255, 14, 12, 255, 14, 13, 255, 14, 18, 255, 14, 19, 255, 14, 20, 255, 14, 21, 255, 14, 22, 255, 14, 23, 255, 14, 24, 255, 14, 25, 255, 15, 7, 255, 15, 8, 255, 15, 9, 255, 15, 10, 255, 15, 11, 255, 15, 12, 255, 15, 19, 255, 15, 20, 255, 15, 21, 255, 15, 22, 255, 15, 23, 255, 15, 24, 255, 15, 18, 255, 7, 6, 255, 7, 13, 255, 7, 18, 255, 7, 25, 255, 15, 6, 255, 15, 13, 255, 15, 25, 255, 8, 5, 255, 8, 14, 255, 8, 26, 255, 9, 5, 255, 9, 14, 255, 9, 17, 255, 9, 26, 255, 10, 5, 255, 10, 14, 255, 10, 17, 255, 10, 26, 255, 11, 5, 255, 11, 14, 255, 11, 17, 255, 11, 26, 255, 12, 5, 255, 12, 14, 255, 12, 17, 255, 12, 26, 255, 13, 5, 255, 13, 14, 255, 13, 17, 255, 13, 26, 255, 14, 14, 255, 14, 17, 255, 6, 21, 255, 6, 22, 255, 7, 5, 255, 7, 26, 255, 8, 17, 255, 14, 5, 255, 14, 26, 255, 15, 14, 255, 15, 17, 255, 15, 26, 255, 6, 6, 255, 6, 7, 255, 6, 8, 255, 6, 9, 255, 6, 10, 255, 6, 11, 255, 6, 12, 255, 6, 13, 255, 6, 18, 255, 6, 19, 255, 6, 20, 255, 6, 23, 255, 6, 24, 255, 6, 25, 255, 7, 14, 255, 7, 17, 255, 15, 5, 255, 16, 7, 255, 16, 8, 255, 16, 9, 255, 16, 10, 255, 16, 11, 255, 16, 12, 255, 16, 19, 255, 16, 20, 255, 16, 21, 255, 16, 22, 255, 16, 23, 255, 16, 24, 255, 16, 25, 255, 6, 6, 0, 6, 7, 0, 6, 8, 0, 6, 9, 0, 6, 10, 0, 6, 11, 0, 6, 12, 0, 6, 13, 0, 6, 18, 0, 6, 19, 0, 6, 20, 0, 6, 21, 0, 6, 22, 0, 6, 23, 0, 6, 24, 0, 6, 25, 0, 7, 14, 0, 7, 17, 0, 15, 5, 0, 15, 14, 0, 15, 17, 0, 15, 26, 0, 16, 7, 0, 16, 12, 0, 16, 25, 0, 7, 5, 0, 7, 6, 0, 7, 9, 0, 7, 10, 0, 7, 13, 0, 7, 18, 0, 7, 21, 0, 7, 22, 0, 7, 25, 0, 7, 26, 0, 8, 5, 0, 8, 14, 0, 8, 17, 0, 8, 26, 0, 9, 5, 0, 9, 14, 0, 9, 17, 0, 9, 26, 0, 10, 5, 0, 10, 14, 0, 10, 17, 0, 10, 26, 0, 11, 5, 0, 11, 14, 0, 11, 17, 0, 11, 26, 0, 12, 5, 0, 12, 14, 0, 12, 17, 0, 12, 26, 0, 13, 5, 0, 13, 14, 0, 13, 17, 0, 13, 26, 0, 14, 5, 0, 14, 6, 0, 14, 14, 0, 14, 17, 0, 14, 25, 0, 14, 26, 0, 15, 6, 0, 15, 13, 0, 15, 18, 0, 15, 25, 0, 16, 8, 0, 16, 11, 0, 16, 19, 0, 16, 20, 0, 16, 23, 0, 16, 24, 0, 7, 11, 0, 7, 12, 0, 7, 19, 0, 7, 20, 0, 8, 6, 0, 8, 13, 0, 8, 18, 0, 8, 25, 0, 11, 6, 0, 11, 25, 0, 12, 6, 0, 12, 13, 0, 12, 18, 0, 12, 25, 0, 13, 6, 0, 13, 13, 0, 13, 18, 0, 13, 25, 0, 14, 7, 0, 14, 12, 0, 14, 13, 0, 14, 18, 0, 14, 19, 0, 14, 24, 0, 15, 7, 0, 15, 8, 0, 15, 12, 0, 15, 19, 0, 15, 24, 0, 7, 9, 255, 7, 11, 255, 7, 20, 255, 7, 22, 255, 9, 6, 0, 9, 25, 0, 10, 6, 0, 10, 25, 0, 11, 13, 0, 11, 18, 0, 13, 7, 0, 13, 24, 0, 15, 11, 0, 15, 20, 0, 15, 23, 0, 16, 9, 0, 7, 9, 0, 7, 11, 0, 7, 20, 0, 7, 22, 0, 8, 25, 255, 9, 6, 255, 9, 25, 255, 10, 6, 255, 10, 25, 255, 11, 13, 255, 11, 18, 255, 7, 7, 0, 7, 8, 0, 7, 23, 0, 7, 24, 0, 8, 6, 255, 11, 6, 255, 11, 25, 255, 12, 13, 255, 12, 18, 255, 13, 7, 255, 13, 24, 255, 16, 22, 0, 9, 5, 255, 9, 26, 255, 10, 5, 255, 10, 26, 255, 12, 6, 255, 12, 25, 255, 15, 11, 255, 15, 20, 255, 7, 7, 255, 7, 24, 255, 11, 5, 255, 11, 26, 255, 13, 13, 255, 13, 18, 255, 14, 12, 255, 14, 19, 255, 14, 24, 255, 15, 23, 255, 16, 10, 0, 16, 21, 0, 10, 14, 255, 10, 17, 255, 11, 14, 255, 11, 17, 255, 13, 25, 255, 14, 7, 255, 10, 17, 0, 13, 25, 0, 14, 7, 0, 7, 7, 0, 10, 14, 0, 11, 5, 0, 11, 14, 0, 11, 17, 0, 11, 26, 0, 13, 13, 0, 13, 18, 0, 14, 12, 0, 14, 19, 0, 14, 24, 0, 15, 23, 0, 16, 21, 255, 7, 24, 0, 9, 5, 0, 9, 26, 0, 10, 5, 0, 10, 26, 0, 12, 6, 0, 15, 11, 0, 15, 20, 0, 16, 10, 255, 16, 22, 255, 7, 7, 255, 7, 8, 255, 7, 23, 255, 7, 24, 255, 8, 6, 0, 11, 6, 0, 11, 25, 0, 12, 13, 0, 12, 18, 0, 12, 25, 0, 13, 7, 0, 7, 9, 255, 7, 11, 255, 7, 20, 255, 7, 22, 255, 8, 25, 0, 9, 6, 0, 10, 6, 0, 10, 25, 0, 11, 13, 0, 11, 18, 0, 13, 24, 0, 7, 9, 0, 7, 11, 0, 7, 20, 0, 9, 6, 255, 10, 6, 255, 10, 25, 255, 11, 13, 255, 11, 18, 255, 7, 7, 0, 7, 8, 0, 7, 22, 0, 7, 23, 0, 7, 24, 0, 8, 6, 255, 8, 25, 255, 11, 6, 255, 11, 25, 255, 12, 13, 255, 12, 18, 255, 12, 25, 255, 13, 7, 255, 13, 24, 255, 16, 22, 0, 7, 7, 255, 7, 24, 255, 9, 5, 255, 9, 26, 255, 10, 5, 255, 10, 26, 255, 11, 5, 255, 11, 26, 255, 12, 6, 255, 14, 12, 255, 14, 19, 255, 14, 24, 255, 15, 11, 255, 15, 20, 255, 15, 23, 255, 16, 10, 0, 16, 21, 0, 10, 14, 255, 10, 17, 255, 11, 14, 255, 11, 17, 255, 13, 13, 255, 13, 18, 255, 13, 25, 255, 14, 7, 255, 13, 25, 0, 14, 7, 0, 10, 14, 0, 10, 17, 0, 11, 14, 0, 11, 17, 0, 13, 13, 0, 13, 18, 0, 14, 24, 0, 11, 5, 0, 15, 23, 0, 7, 7, 0, 11, 26, 0, 14, 12, 0, 14, 19, 0, 16, 21, 255, 9, 5, 0, 7, 24, 0, 16, 10, 255, 9, 26, 0, 10, 5, 0, 10, 26, 0, 15, 11, 0, 15, 20, 0, 7, 8, 255, 7, 23, 255, 7, 24, 255, 12, 6, 0, 12, 13, 0, 12, 18, 0, 12, 25, 0, 16, 22, 255, 7, 7, 255, 11, 6, 0, 11, 25, 0, 13, 7, 0, 7, 9, 255, 7, 22, 255, 8, 6, 0, 8, 25, 0, 11, 13, 0, 13, 24, 0, 7, 11, 255, 7, 20, 255, 9, 6, 0, 10, 6, 0, 10, 25, 0, 11, 18, 0, 7, 11, 0, 7, 20, 0, 9, 6, 255, 10, 25, 255, 11, 13, 255, 7, 9, 0, 7, 22, 0, 10, 6, 255, 11, 18, 255, 8, 6, 255, 8, 25, 255, 11, 6, 255, 11, 25, 255, 13, 7, 255, 13, 24, 255, 7, 7, 0, 7, 24, 0, 12, 13, 255, 12, 18, 255, 7, 8, 0, 7, 23, 0, 12, 6, 255, 12, 25, 255, 16, 22, 0, 10, 26, 255, 15, 11, 255, 15, 20, 255, 9, 5, 255, 9, 26, 255, 10, 5, 255, 16, 10, 0, 7, 7, 255, 7, 24, 255, 11, 5, 255, 11, 26, 255, 14, 12, 255, 14, 19, 255, 16, 21, 0, 13, 18, 255, 14, 24, 255, 15, 23, 255, 10, 14, 255, 10, 17, 255, 11, 14, 255, 11, 17, 255, 13, 13, 255, 13, 25, 255, 14, 7, 255, 10, 14, 0, 10, 17, 0, 11, 14, 0, 11, 17, 0, 13, 13, 0, 13, 18, 0, 13, 25, 0, 14, 7, 0, 7, 7, 0, 7, 24, 0, 11, 5, 0, 11, 26, 0, 14, 12, 0, 14, 19, 0, 14, 24, 0, 15, 23, 0, 16, 21, 255, 9, 5, 0, 9, 26, 0, 10, 5, 0, 10, 26, 0, 15, 11, 0, 15, 20, 0, 16, 10, 255, 7, 8, 255, 7, 23, 255, 7, 24, 255, 12, 6, 0, 12, 13, 0, 12, 18, 0, 12, 25, 0, 16, 22, 255, 7, 7, 255, 8, 6, 0, 11, 6, 0, 11, 25, 0, 13, 7, 0, 13, 24, 0, 7, 9, 255, 7, 11, 255, 7, 20, 255, 7, 22, 255, 8, 25, 0, 9, 6, 0, 10, 6, 0, 10, 25, 0, 11, 13, 0, 11, 18, 0, 9, 25, 0, 16, 9, 255, 9, 6, 255, 9, 25, 255, 10, 25, 255, 11, 13, 255, 11, 18, 255, 15, 11, 255, 15, 20, 255, 7, 9, 0, 7, 11, 0, 7, 20, 0, 7, 22, 0, 8, 6, 255, 8, 25, 255, 10, 6, 255, 11, 6, 255, 11, 25, 255, 12, 13, 255, 12, 18, 255, 13, 7, 255, 13, 24, 255, 14, 7, 255, 14, 12, 255, 14, 19, 255, 14, 24, 255, 15, 8, 255, 15, 23, 255, 7, 11, 255, 7, 12, 255, 7, 19, 255, 7, 20, 255, 8, 13, 255, 8, 18, 255, 12, 6, 255, 12, 25, 255, 13, 6, 255, 13, 13, 255, 13, 18, 255, 13, 25, 255, 15, 7, 255, 15, 12, 255, 15, 19, 255, 15, 24, 255, 7, 6, 255, 7, 9, 255, 7, 10, 255, 7, 13, 255, 7, 18, 255, 7, 21, 255, 7, 22, 255, 7, 25, 255, 9, 26, 255, 10, 5, 255, 10, 26, 255, 11, 5, 255, 11, 14, 255, 11, 26, 255, 14, 6, 255, 14, 13, 255, 14, 18, 255, 14, 25, 255, 15, 6, 255, 15, 13, 255, 15, 18, 255, 15, 25, 255, 16, 11, 255, 16, 20, 255, 16, 23, 255, 7, 5, 255, 7, 26, 255, 8, 5, 255, 8, 14, 255, 8, 17, 255, 8, 26, 255, 9, 5, 255, 9, 14, 255, 9, 17, 255, 10, 14, 255, 10, 17, 255, 11, 17, 255, 12, 5, 255, 12, 14, 255, 12, 17, 255, 12, 26, 255, 13, 5, 255, 13, 14, 255, 13, 17, 255, 13, 26, 255, 14, 5, 255, 14, 14, 255, 14, 17, 255, 14, 26, 255, 16, 8, 255, 16, 24, 255, 6, 6, 255, 6, 7, 255, 6, 8, 255, 6, 9, 255, 6, 10, 255, 6, 11, 255, 6, 12, 255, 6, 19, 255, 6, 20, 255, 6, 21, 255, 6, 22, 255, 6, 23, 255, 6, 24, 255, 6, 25, 255, 7, 14, 255, 7, 17, 255, 15, 5, 255, 15, 14, 255, 15, 17, 255, 15, 26, 255, 16, 7, 255, 16, 12, 255, 16, 19, 255, 6, 18, 255, 6, 18, 0, 16, 7, 0, 16, 8, 0, 16, 9, 0, 16, 10, 0, 16, 11, 0, 16, 12, 0, 16, 19, 0, 16, 20, 0, 16, 21, 0, 16, 22, 0, 6, 6, 0, 6, 7, 0, 6, 8, 0, 6, 9, 0, 6, 10, 0, 6, 11, 0, 6, 12, 0, 6, 19, 0, 6, 20, 0, 6, 21, 0, 6, 22, 0, 6, 23, 0, 6, 24, 0, 6, 25, 0, 7, 14, 0, 7, 17, 0, 15, 5, 0, 15, 14, 0, 15, 17, 0, 15, 26, 0, 16, 23, 0, 16, 24, 0, 7, 5, 0, 7, 26, 0, 8, 14, 0, 8, 17, 0, 14, 5, 0, 14, 14, 0, 14, 17, 0, 14, 26, 0, 8, 5, 0, 8, 26, 0, 9, 5, 0, 9, 14, 0, 9, 17, 0, 9, 26, 0, 10, 5, 0, 10, 14, 0, 10, 17, 0, 11, 5, 0, 12, 5, 0, 12, 14, 0, 12, 26, 0, 13, 5, 0, 13, 14, 0, 13, 17, 0, 13, 26, 0, 10, 26, 0, 11, 14, 0, 11, 17, 0, 11, 26, 0, 12, 17, 0, 7, 6, 0, 15, 6, 0, 15, 25, 0, 7, 13, 0, 7, 18, 0, 7, 25, 0, 15, 13, 0, 15, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

unsigned char *animacion;
unsigned char n_frames;
unsigned char lista_cambios[120];
unsigned int last;
unsigned int actual_frame;
unsigned char* lista_animaciones[8];

void setup() {

  // Animaciones
  Serial.begin(9600);

  pinMode(8, INPUT);
  
  // Preparando pantalla
  myGLCD.InitLCD();
  myGLCD.clrScr();
  
  lista_animaciones[0] = &enfadado[0];
  lista_animaciones[1] = &corazon[0];
  
  load_new_animation(enfadado);

}

inline void load_new_animation(unsigned char* newAnimation) {
  myGLCD.clrScr();
  //free(animacion);
  animacion = newAnimation;
  n_frames = pgm_read_byte_near(animacion);
  for (int i = 0; i < n_frames; i++) {
    lista_cambios[i] = pgm_read_byte_near(animacion + 1 + i);
  }
  last = 1 + n_frames;
  actual_frame = 0;
}

unsigned char old_input = 0;

inline unsigned char read_input() {
  unsigned char a = 1 * (digitalRead(8)  == HIGH)?1:0;
  unsigned char b = 2 * (digitalRead(9)  == HIGH)?0:0;
  unsigned char c = 4 * (digitalRead(10) == HIGH)?0:0;
  unsigned char res = a+b+c;
  Serial.println(res);
  return res;
}

void loop() {
  Serial.println(freeMemory());
  unsigned char animacion_nueva = read_input();
  if (animacion_actual !=  animacion_nueva) {
    
    load_new_animation(lista_animaciones[animacion_nueva]);
    animacion_actual = animacion_nueva;
  }else {
    // Renderizamos los frames
    if (actual_frame == n_frames) {
      actual_frame = 0;
      last = 1 + n_frames;
    }
  
    for (int j = 0; j < lista_cambios[actual_frame]; j++) {
   unsigned char color = pgm_read_byte_near(animacion + last + 2);
   myGLCD.setColor(color, color, color);
   myGLCD.fillRoundRect(pgm_read_byte_near(animacion + last + 1) * 10,
     pgm_read_byte_near(animacion + last) * 10,
     pgm_read_byte_near(animacion + last + 1) * 10 + 10,
     pgm_read_byte_near(animacion + last) * 10 + 10);
   last += 3;
  }
  actual_frame++;
  
  delay(20);
  }
  
  
}
