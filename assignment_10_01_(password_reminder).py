# -*- coding: utf-8 -*-
"""Assignment - 10/01 (Password Reminder)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S6agzWAowsAgDJ_qXgJvH-RdKadiASeP
"""





isim = input("İSMİNİ GİR :").capitalize()
if isim == "Hasan":
  print("Hello, Hasan! The password is : W@12")
else:
  print("Hello, {}! See you later.".format(isim))