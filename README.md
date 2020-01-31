<h1 align="center">
  <br>
  <a href="https://github.com/SmoZy92/Office365-verify"><img src="https://i.imgur.com/lBMyNrN.png" alt="O365"></a>
  <br>
  Office 365 enumerator
  <br>
</h1>

<h4 align="center">Verify Office 365 email addresses</h4>


### Introduction
This program uses the autodiscover JSON API of Office 365 to enumerate valid email addresses from a text file as fast as possible with multi threading.
Office 365 enumerator can see if an email address is valid in Office365. This does not perform any login attempts, is unthrottled, and is incredibly useful for social engineering assessments to find which emails exist and which don't.

![demo](https://i.imgur.com/sVjnHrC.png)

### Requirements
Office 365 enumerator works with a go script created by Jakewarren (https://github.com/jakewarren/o365verify/tree/bfe37aca392d606584648a97845d5454f239813d)


### Usage
Using office 365 enumerator is pretty simple

`python o365enum.py emails.txt 10`


### Credits
- Jakewarren (https://github.com/jakewarren/o365verify/tree/bfe37aca392d606584648a97845d5454f239813d)
- Raikia (https://github.com/Raikia/UhOh365/tree/4494adb681051ef317d82e7b887c7806acf89a42)
- 0xZDH (https://github.com/0xZDH/o365spray/tree/a69a9c7859a3e27b527d1ec00bbac27ac97b1fd5)

