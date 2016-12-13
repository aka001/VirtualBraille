# VirtualBraille

**Team Members:** (github handles) [All have equal contribution] 
1. Akash Agrawall (aka001)  
2. Ashish Kumar (ashishkumar1993)  
3. Rohit SVK (rohitsakala)  
4. Smriti Jain (smriti100jain)  


**Idea:**

To develop a personal assistant for Visually Imapired. The personal assistant included basic utilities like --  
1. Color announcer – Will announce the color seen in the camera.  
2. Printed Text to Speech – Will convert printed text visible through the camera to speech.  
3. Printed Text to braille – Will convert the character visible through the camera to braille output on a 6-dot pad.  
4. Edge Detector – Will generate a vibration whenever the camera sees an outline in a drawn image.  
For Example, if a rectangle is drawn on a paper, the camera will vibrate when it is held above any edge of the rectangle. This will give the blind, a sense of the objects drawn on paper.  

**Our Visit to the Blind People's Association:**  

1. Those who are not born with visual impairment and lose their sight due to an accident were more inclined towards printed text to speech, where as those who were blind since birth wanted to read in braille. Reading has the advantage of easy navigation, getting a knowledge of spellings and other details of any written language.  
2. They did not like depending on others for help. They were not comfortable with other's knowing that they are visually impaired.  

**Our Product Design and Implementation:**  

We used Raspberry Pi along with its camera module to develop the handheld hardware. The python code for color announcer, printed text to speech and edge detector was then copied to the Raspberry Pi. The Raspberry Pi had Debian installed in its memory card.  

The vibrator motor was attached to the conditional output of Raspberry Pi and was responsible for generating the output vbration in case of an edge detector.
