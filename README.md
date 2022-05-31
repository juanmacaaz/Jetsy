<img src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/jetsy.png" align="right" width="300" alt="header pic"/>

# Jetsy
![GitHub_Action_Linux_CI](https://github.com/AtsushiSakai/PythonRobotics/workflows/Linux_CI/badge.svg)
[![Build status](https://ci.appveyor.com/api/projects/status/sb279kxuv1be391g?svg=true)](https://ci.appveyor.com/project/AtsushiSakai/pythonrobotics)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/AtsushiSakai/PythonRobotics.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/AtsushiSakai/PythonRobotics/context:python)

Personal assistant robot that interacts with the human being on a physical and emotional level.

# Table of Contents
   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
   * [Components](#components)
   * [Eyes](#eyes)
      * [Affirmation](#affirmation)
      * [Loved](#loved)
      * [Suspicious](#suspicious)
      * [Angry](#angry)
      * [Happy](#happy)
      * [Normal](#normal)
      * [Sad](#sad)
   * [Arms](#arms)
      * [Up](#up)
      * [Left](#left)
      * [Right](#right)
      * [Down](#down)
   * [Movements](#moviments)
      * [Go](#Go)
      * [Left](#Left)
      * [Right](#Right)
      * [Back](#Back)
   * [Proximity Sensors](#proximity-sensors)
      * [Frontal](#frontal-proximity-sensors)
      * [Floor](#floor-proximity-sensors)
   * [Command Voice](#command-voice)
      * [Voice Controller](#voice-controller)
      * [Dance](#dance)
      * [Repeat](#repeat)
      * [Tell me a joke](#tell-me-a-joke)
      * [Emotion Detection](#emotional-detection)
      * [Where I am](#where-i-am)
      * [Object Classification](#object-classification)
   * [Built With](#built-with)
   * [License](#license)
   * [Use-case](#use-case)
   * [Contribution](#contribution)
   * [Citing](#citing)
   * [Support](#support)
   * [Authors](#authors)
   * [Bibliography](#bibliography)



# What is this?
This project seeks to create an autonomous robot completely focused on emotional interaction with the user. It will be carried out by means of a table assistant with already existing typical functionalities, but thanks to artificial intelligence you will be able to interact with it through voice and video and thus enhance robot-human interaction seeking the maximum fluidity possible.

We also believe that the aesthetic design of the robot is very important to be able to transmit emotions to the user, so it will be very well worked.

Another point that we want is that all software has to be open source, from deep learning models to used libraries. You do not need an internet connection to use most of its features.

# Requirements

For running each sample code:

- [Python 3.9.x](https://www.python.org/)

- [pytorch](https://pytorch.org/)
- [opencv](https://opencv.org/)
- [pipwin](https://pypi.org/project/pipwin/)
- [pyaudio](https://pypi.org/project/PyAudio/)
- [pygame](https://www.pygame.org/)
- [torchaudio](https://pytorch.org/audio/)
- [omegaconf](https://omegaconf.readthedocs.io/)
- [sox](https://pypi.org/project/sox/)
- [noisereduce](https://pypi.org/project/noisereduce/)
- [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)

# How to use

1. Clone this repo.

> git clone https://github.com/juanmacaaz/Jetsy

2. Go to the directory where the code is located.

> cd Jesty

3. Install the required libraries.
 
using pip :

> pip install -r Requirements/requirements.txt

4. Execute the following command to run the sample code.

> python3 run.py

5. Add star to this repo if you like it :smiley:. 

# Components
<table align="center" border="0">
<tr>

<td align="center">

[SainSmart Dysplay](https://www.amazon.com/-/es/SainSmart-Display-adaptador-Arduino-2560-Nano/dp/B008FWSG3S)
</td><td align="center">

[Raspberry Pi Camera](https://es.aliexpress.com/item/4001162865845.html?spm=a2g0o.ppclist.product.2.3d91WN0rWN0rwh&pdp_npi=2%40dis%21EUR%21%E2%82%AC%203%2C69%21%E2%82%AC%202%2C76%21%21%21%21%21%40211b5dfd16539403796157400e6948%2112000018174400524%21btf&_t=pvid%3A9a5ddde9-5795-4052-80bd-c3985eeb8d6a&afTraceInfo=4001162865845__pc__pcBridgePPC__xxxxxx__1653940380&gatewayAdapt=glo2esp)
</td><td align="center">

[Sg90](https://es.aliexpress.com/item/1005001943420922.html?spm=a2g0o.ppclist.product.2.442fNuE5NuE5NS&_t=pvid%3A0529091f-a660-4dab-8e19-41a022528d75&afTraceInfo=1005001943420922__pc__pcBridgePPC__xxxxxx__1653940575&gatewayAdapt=glo2esp)
</td><td align="center">

[GA12-N20 DC](https://es.aliexpress.com/item/1005003480074662.html?spm=a2g0o.ppclist.product.4.6653uf4muf4mln&pdp_npi=2%40dis%21EUR%21%E2%82%AC%202%2C11%21%E2%82%AC%201%2C69%21%21%21%21%21%400b0a2e9c16539413541178310ee236%2112000025975341302%21btf&_t=pvid%3A383536ed-b61b-4b24-8b09-32b6c2c69a4d&afTraceInfo=1005003480074662__pc__pcBridgePPC__xxxxxx__1653941354&gatewayAdapt=glo2esp)
</td></tr>

<tr>
    <td align="center">
        <a href="https://www.amazon.com/-/es/SainSmart-Display-adaptador-Arduino-2560-Nano/dp/B008FWSG3S" target="_blank"><img border="0" src="https://m.media-amazon.com/images/I/81GVEWT4HDL._AC_SL1500_.jpg" ></a>
        <img src="https://ir-na.amazon-adsystem.com/e/ir?t=vmw0a-20&l=li2&o=1&a=B01HDC236Q" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.amazon.com/gp/product/B00KH07WRC/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=vmw0a-20&linkId=52a63711f582d1ff83f4687137a6154b" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/HLB1vgG5UAPoK1RjSZKbq6x1IXXaN/C-mara-Raspberry-Pi-5MP-1080P-OV5647-c-mara-web-m-dulo-de-c-mara-con.jpg_Q90.jpg_.webp" ></a>
        <img src="https://es.aliexpress.com/item/1005001943420922.html?spm=a2g0o.ppclist.product.2.442fNuE5NuE5NS&_t=pvid%3A0529091f-a660-4dab-8e19-41a022528d75&afTraceInfo=1005001943420922__pc__pcBridgePPC__xxxxxx__1653940575&gatewayAdapt=glo2esp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://es.aliexpress.com/item/1005001943420922.html?spm=a2g0o.ppclist.product.2.442fNuE5NuE5NS&_t=pvid%3A0529091f-a660-4dab-8e19-41a022528d75&afTraceInfo=1005001943420922__pc__pcBridgePPC__xxxxxx__1653940575&gatewayAdapt=glo2esp" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/H952b94f0cdf845fa8d2ace607daa32a2u/Micro-Motor-Servo-Sg90-9g-para-Robot-de-control-remoto-6-canales-9g-Sg90-Servo-Motor.jpg_Q90.jpg_.webp" ></a>
        <img src="https://ae01.alicdn.com/kf/H952b94f0cdf845fa8d2ace607daa32a2u/Micro-Motor-Servo-Sg90-9g-para-Robot-de-control-remoto-6-canales-9g-Sg90-Servo-Motor.jpg_Q90.jpg_.webp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://es.aliexpress.com/item/1005003480074662.html?spm=a2g0o.ppclist.product.4.6653uf4muf4mln&pdp_npi=2%40dis%21EUR%21%E2%82%AC%202%2C11%21%E2%82%AC%201%2C69%21%21%21%21%21%400b0a2e9c16539413541178310ee236%2112000025975341302%21btf&_t=pvid%3A383536ed-b61b-4b24-8b09-32b6c2c69a4d&afTraceInfo=1005003480074662__pc__pcBridgePPC__xxxxxx__1653941354&gatewayAdapt=glo2esp" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/H3f969b492dae4c5a8433b1bcd2af8f8ds/GA12-N20-DC-3V-6V-12V-Micro-Motor-de-engranaje-de-Metal-30RPM-50RPM-60RPM-100RPM.jpg_Q90.jpg_.webp" ></a>
        <img src="https://ae01.alicdn.com/kf/H3f969b492dae4c5a8433b1bcd2af8f8ds/GA12-N20-DC-3V-6V-12V-Micro-Motor-de-engranaje-de-Metal-30RPM-50RPM-60RPM-100RPM.jpg_Q90.jpg_.webp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
</tr>

<tr>

<td align="center">

[infrared barrier module](https://es.aliexpress.com/item/32903218497.html?spm=a2g0o.ppclist.product.16.400a4UpR4UpRPV&_t=pvid%3Ac90bf613-2ff6-44b0-a6d5-22b7c9a34ed7&afTraceInfo=32903218497__pc__pcBridgePPC__xxxxxx__1653941607&gatewayAdapt=glo2esp)
</td><td align="center">

[infrared barrier module](https://es.aliexpress.com/item/1005001621744601.html?spm=a2g0o.ppclist.product.90.400a4UpR4UpRPV&pdp_npi=2%40dis%21EUR%21%E2%82%AC%200%2C59%21%E2%82%AC%200%2C47%21%21%21%21%21%400b0a24a616539416371568688e6422%2112000016846397267%21btf&_t=pvid%3Acb3d0e9f-6a7b-4e75-b2b4-a89adac397b2&afTraceInfo=1005001621744601__pc__pcBridgePPC__xxxxxx__1653941637&gatewayAdapt=glo2esp)
</td><td align="center">

[L298N](https://www.amazon.es/Neuftech-Puente-conductor-controlador-arduino/dp/B01KBTNHS6/ref=asc_df_B01KBTNHS6/?tag=googshopes-21&linkCode=df0&hvadid=82869581890&hvpos=&hvnetw=g&hvrand=4904570669855784615&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-276836500057&psc=1)
</td><td align="center">

[Plastic AA Battery Holder](https://es.aliexpress.com/item/1005001866700713.html?spm=a2g0o.ppclist.product.2.268fUa6kUa6kcJ&_t=pvid%3A4b8f1796-ebef-4ebe-b95d-6729a2ef8c31&afTraceInfo=1005001866700713__pc__pcBridgePPC__xxxxxx__1653941884&gatewayAdapt=glo2esp)
</td></tr>

<tr>
    <td align="center">
        <a href="https://es.aliexpress.com/item/32903218497.html?spm=a2g0o.ppclist.product.16.400a4UpR4UpRPV&_t=pvid%3Ac90bf613-2ff6-44b0-a6d5-22b7c9a34ed7&afTraceInfo=32903218497__pc__pcBridgePPC__xxxxxx__1653941607&gatewayAdapt=glo2esp" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/HTB11gvCXCSD3KVjSZFKq6z10VXax/M-dulo-de-Sensor-de-evitaci-n-de-obst-culos-dispositivo-infrarrojo-IR-para-Arduino-Smart.jpg_Q90.jpg_.webp" ></a>
        <img src="https://es.aliexpress.com/item/32903218497.html?spm=a2g0o.ppclist.product.16.400a4UpR4UpRPV&_t=pvid%3Ac90bf613-2ff6-44b0-a6d5-22b7c9a34ed7&afTraceInfo=32903218497__pc__pcBridgePPC__xxxxxx__1653941607&gatewayAdapt=glo2esp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://es.aliexpress.com/item/1005001621744601.html?spm=a2g0o.ppclist.product.90.400a4UpR4UpRPV&pdp_npi=2%40dis%21EUR%21%E2%82%AC%200%2C59%21%E2%82%AC%200%2C47%21%21%21%21%21%400b0a24a616539416371568688e6422%2112000016846397267%21btf&_t=pvid%3Acb3d0e9f-6a7b-4e75-b2b4-a89adac397b2&afTraceInfo=1005001621744601__pc__pcBridgePPC__xxxxxx__1653941637&gatewayAdapt=glo2esp" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/H8095ff2f958c41638e0b52c032a0659cQ/Sensor-reflectante-infrarrojo-TCRT5000-interruptor-fotoel-ctrico-IR-m-dulo-de-pista-de-l-nea-de.jpg_Q90.jpg_.webp" ></a>
        <img src="https://es.aliexpress.com/item/1005001621744601.html?spm=a2g0o.ppclist.product.90.400a4UpR4UpRPV&pdp_npi=2%40dis%21EUR%21%E2%82%AC%200%2C59%21%E2%82%AC%200%2C47%21%21%21%21%21%400b0a24a616539416371568688e6422%2112000016846397267%21btf&_t=pvid%3Acb3d0e9f-6a7b-4e75-b2b4-a89adac397b2&afTraceInfo=1005001621744601__pc__pcBridgePPC__xxxxxx__1653941637&gatewayAdapt=glo2esp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.amazon.es/Neuftech-Puente-conductor-controlador-arduino/dp/B01KBTNHS6/ref=asc_df_B01KBTNHS6/?tag=googshopes-21&linkCode=df0&hvadid=82869581890&hvpos=&hvnetw=g&hvrand=4904570669855784615&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-276836500057&psc=1" target="_blank"><img border="0" src="https://m.media-amazon.com/images/I/71djDWh1BJL._AC_SX679_.jpg" ></a>
        <img src="https://www.amazon.es/Neuftech-Puente-conductor-controlador-arduino/dp/B01KBTNHS6/ref=asc_df_B01KBTNHS6/?tag=googshopes-21&linkCode=df0&hvadid=82869581890&hvpos=&hvnetw=g&hvrand=4904570669855784615&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-276836500057&psc=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://es.aliexpress.com/item/1005001866700713.html?spm=a2g0o.ppclist.product.2.268fUa6kUa6kcJ&_t=pvid%3A4b8f1796-ebef-4ebe-b95d-6729a2ef8c31&afTraceInfo=1005001866700713__pc__pcBridgePPC__xxxxxx__1653941884&gatewayAdapt=glo2esp" target="_blank"><img border="0" src="https://ae01.alicdn.com/kf/Hb76af52866704c0fbf51369b59cd0ab3h/Soporte-de-bater-a-AA-de-pl-stico-caja-de-doble-cara-con-resorte-trasero-con.jpg_Q90.jpg_.webp" ></a>
        <img src="https://es.aliexpress.com/item/1005001866700713.html?spm=a2g0o.ppclist.product.2.268fUa6kUa6kcJ&_t=pvid%3A4b8f1796-ebef-4ebe-b95d-6729a2ef8c31&afTraceInfo=1005001866700713__pc__pcBridgePPC__xxxxxx__1653941884&gatewayAdapt=glo2esp" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
</tr>

<tr>

<td align="center">

[Arduino Uno](https://es.farnell.com/arduino/k010007/starter-kit-arduino-uno-board/dp/2356913?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n4NDbeu6vhVgvoaujFOr0psZl7O5Cq9CFvkzVDsqh5MlO6WXkxoKkaAkHUEALw_wcB&mckv=sar3wjxWV_dc%7Cpcrid%7C491017246442%7Cplid%7C%7Ckword%7C%7Cmatch%7C%7Cslid%7C%7Cproduct%7C2356913%7Cpgrid%7C111938091822%7Cptaid%7Cpla-402461644477&CMP=KNC-GES-GEN-SHOPPING-SMEC-Whoops-Medium-Desktop-Title-Changes-10-Aug-21&gross_price=true)
</td><td align="center">

[Power Bank](https://www.amazon.es/Ekrist-26800mAh-Portatil-Powerbank-Cargador/dp/B07TQ43RY2?th=1)
</td><td align="center">

[Switch On / Off](https://www.carrefour.es/mini-altavoz-innova-wireless-innsoul-alt-37/VC4A-17700772/p?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n-dVVxX-pnJ5jLpnMJxUPTb12rfhr-3RFtsztOfxjNbZOv8wsuDQgaAm45EALw_wcB&gclsrc=aw.ds)
</td><td align="center">

[USB Microphone](https://www.amazon.es/Micr%C3%B3fono-Seacue-Omnidireccional-Condensador-Entrevistas/dp/B071171DBP/ref=asc_df_B071171DBP/?tag=googshopes-21&linkCode=df0&hvadid=301089040287&hvpos=&hvnetw=g&hvrand=14783442952137543429&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-378893081924&psc=1)
</td></tr>

<tr>
    <td align="center">
        <a href="https://es.farnell.com/arduino/k010007/starter-kit-arduino-uno-board/dp/2356913?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n4NDbeu6vhVgvoaujFOr0psZl7O5Cq9CFvkzVDsqh5MlO6WXkxoKkaAkHUEALw_wcB&mckv=sar3wjxWV_dc%7Cpcrid%7C491017246442%7Cplid%7C%7Ckword%7C%7Cmatch%7C%7Cslid%7C%7Cproduct%7C2356913%7Cpgrid%7C111938091822%7Cptaid%7Cpla-402461644477&CMP=KNC-GES-GEN-SHOPPING-SMEC-Whoops-Medium-Desktop-Title-Changes-10-Aug-21&gross_price=true" target="_blank"><img border="0" src="https://image.made-in-china.com/2f0j00ylEfKvtsgpku/Arduino-Uno-R3-Development-Board-Microcontroller-for-DIY-Project.jpg"></a>
        <img src="https://es.farnell.com/arduino/k010007/starter-kit-arduino-uno-board/dp/2356913?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n4NDbeu6vhVgvoaujFOr0psZl7O5Cq9CFvkzVDsqh5MlO6WXkxoKkaAkHUEALw_wcB&mckv=sar3wjxWV_dc%7Cpcrid%7C491017246442%7Cplid%7C%7Ckword%7C%7Cmatch%7C%7Cslid%7C%7Cproduct%7C2356913%7Cpgrid%7C111938091822%7Cptaid%7Cpla-402461644477&CMP=KNC-GES-GEN-SHOPPING-SMEC-Whoops-Medium-Desktop-Title-Changes-10-Aug-21&gross_price=true" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.amazon.es/Ekrist-26800mAh-Portatil-Powerbank-Cargador/dp/B07TQ43RY2?th=1" target="_blank"><img border="0" src="https://m.media-amazon.com/images/I/61iGJGT9tvL._AC_SX679_.jpg" ></a>
        <img src="https://www.amazon.es/Ekrist-26800mAh-Portatil-Powerbank-Cargador/dp/B07TQ43RY2?th=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.carrefour.es/mini-altavoz-innova-wireless-innsoul-alt-37/VC4A-17700772/p?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n-dVVxX-pnJ5jLpnMJxUPTb12rfhr-3RFtsztOfxjNbZOv8wsuDQgaAm45EALw_wcB&gclsrc=aw.ds" target="_blank"><img border="0" src="https://static.carrefour.es/hd_510x_/crs/cdn_static/catalog/hd/429715_00_1.jpg" ></a>
        <img src="https://www.carrefour.es/mini-altavoz-innova-wireless-innsoul-alt-37/VC4A-17700772/p?gclid=Cj0KCQjw1tGUBhDXARIsAIJx01n-dVVxX-pnJ5jLpnMJxUPTb12rfhr-3RFtsztOfxjNbZOv8wsuDQgaAm45EALw_wcB&gclsrc=aw.ds" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://www.amazon.es/Micr%C3%B3fono-Seacue-Omnidireccional-Condensador-Entrevistas/dp/B071171DBP/ref=asc_df_B071171DBP/?tag=googshopes-21&linkCode=df0&hvadid=301089040287&hvpos=&hvnetw=g&hvrand=14783442952137543429&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-378893081924&psc=1" target="_blank"><img border="0" src="https://m.media-amazon.com/images/I/61aLrDHYj+L._AC_SX679_.jpg" ></a>
        <img src="https://www.amazon.es/Micr%C3%B3fono-Seacue-Omnidireccional-Condensador-Entrevistas/dp/B071171DBP/ref=asc_df_B071171DBP/?tag=googshopes-21&linkCode=df0&hvadid=301089040287&hvpos=&hvnetw=g&hvrand=14783442952137543429&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1005424&hvtargid=pla-378893081924&psc=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
</tr>

<tr>

<td align="center">

[Front cover](https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo1.stl)
</td><td align="center">

[Back cover](https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo2.stl)
</td><td align="center">

[Arms](https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/brazos.stl)
</td><td align="center">

[Battery Cover](https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/tapa.stl)
</td></tr>

<tr>
    <td align="center">
        <a href="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo1.stl" target="_blank"><img border="0" src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Covers/frontal.png"></a>
        <img src="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo1.stl" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo2.stl" target="_blank"><img border="0" src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Covers/back.png" ></a>
        <img src="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/cuerpo2.stl" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/brazos.stl" target="_blank"><img border="0" src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Covers/arms.png" ></a>
        <img src="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/brazos.stl" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
    <td align="center">
        <a href="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/tapa.stl" target="_blank"><img border="0" src="https://github.com/juanmacaaz/Jetsy/blob/main/Resources/Covers/battery_cover.png" ></a>
        <img src="https://github.com/juanmacaaz/Jetsy/blob/main/HardwareDesign/Models/tapa.stl" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
    </td>
</tr>

<tr><td colspan="4">

# Eyes
## Affirmation
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/affirmation.gif" width="640" alt="affirmation pic">

## Loved
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/loves.gif" width="640" alt="loves pic">

## Suspicious
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/suspicius.gif" width="640" alt="suspicius pic">

## Angry
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/angry.gif" width="640" alt="angry pic">

## Happy
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/happy.gif" width="640" alt="happy pic">

## Normal
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/normal.gif" width="640" alt="normal pic">

## Sad
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Eyes/sad.gif" width="640" alt="sad pic">

# Arms
## Up
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Arms/up.gif" width="640" alt="up pic">

## Left
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Arms/left.gif" width="640" alt="left pic">

## Right
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Arms/right.gif" width="640" alt="right pic">

## Down
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Arms/affirmation.gif" width="640" alt="affirmation pic">

# Moviments
## Go
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Moviments/go.gif" width="640" alt="go pic">

## Left
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Moviments/left.gif" width="640" alt="left pic">

## Right
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Moviments/right.gif" width="640" alt="right pic">

## Back
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Moviments/back.gif" width="640" alt="back pic">

# Proximity-Sensors
## Frontal
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Proximity_Sensors/frontal.gif" width="640" alt="frontal pic">

## Floor
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/Proximity_Sensors/floor.gif" width="640" alt="floor pic">

# Command Voice
## Voice Controller
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/voice_controller.gif" width="640" alt="voice_controller pic">

## Dance
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/dance.gif" width="640" alt="dance pic">

## Repeat
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/repeat.gif" width="640" alt="repeat pic">

## Tell me a joke
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/tell_me_a_joke.gif" width="640" alt="tell_me_a_joke pic">

## Emotion Detection
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/emotion_detection.gif" width="640" alt="emotion_detection pic">

## Where I am
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/where_i_am.gif" width="640" alt="where_i_am pic">

## Object Classification
<img src="https://github.com/juanmacaaz/Jetsy/tree/main/Resources/command_voice/object_classification.gif" width="640" alt="object_classification pic">

# Built With
- [TinkerCard](https://www.tinkercad.com/) - Model Design Program.
- [Arduino](https://www.arduino.cc/) - IDE used for the development of the servos.
- [VSCode](https://code.visualstudio.com/) - Code editor to program hardware components.
- [Python](https://www.python.org/) - Language used for programming.
- [Adoble Suit](https://www.adobe.com/) - For visual content creation.
# License
This project is under the MIT License - see the [LICENSE](https://github.com/juanmacaaz/Jetsy/blob/main/LICENSE.md) file for details

# Use-Case
If this project helps your robotics project, please let us know with creating an issue.

# Contribution
Any contribution is welcome!! 

Contact us via [email](mailto:juanma.caaz@gmail.com).
# Citing
If you use this project's code for your academic work or in industry, we'd love to hear from you as well; feel free to reach out to the developers directly.
# Support 
- [Escola d'Enginyeria - UAB Barcelona](https://www.uab.cat/enginyeria/)
# Authors
* **Juan Manuel Camara** - [juanmacaaz](https://github.com/juanmacaaz)
* **Miguel del Arco** - [migueldemollet](https://github.com/migueldemollet)
* **Daniel Suarez** - [Danny-8](https://github.com/Danny-8)
* **Christian Ferre** - [christian-ferre](https://github.com/christian-ferre)

# Bibliography
- [Controlar un servo con arduino, Luis Llamas, 2016](https://www.luisllamas.es/controlar-un-servo-con-arduino/)
- [Modulo sensor de llama, Andrés Cortés, 2021](https://acortes.co/proyecto-14-modulo-sensor-de-llama/)
- [Tutorial de uso del modulo l298n, Naylamp Mechatronics, 2017](https://naylampmechatronics.com/blog/11_tutorial-de-uso-del-modulo-l298n.html)
- [CSI Camera, Jetson Hacks Nano, 2019](https://github.com/JetsonHacksNano/CSI-Camera)
