{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOtco7S3hPM0p+q42NgcDzQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LakshyaKr0008/piechart/blob/main/message_bot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pyautogui\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5CbaaKQ3U-pu",
        "outputId": "3910cfb6-fcb3-45ff-dd86-c56e167a32cc"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pyautogui\n",
            "  Downloading PyAutoGUI-0.9.54.tar.gz (61 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/61.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[90m╺\u001b[0m\u001b[90m━━━━━━\u001b[0m \u001b[32m51.2/61.2 kB\u001b[0m \u001b[31m2.7 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m61.2/61.2 kB\u001b[0m \u001b[31m1.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting python3-Xlib (from pyautogui)\n",
            "  Downloading python3-xlib-0.15.tar.gz (132 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m132.8/132.8 kB\u001b[0m \u001b[31m4.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting pymsgbox (from pyautogui)\n",
            "  Downloading PyMsgBox-1.0.9.tar.gz (18 kB)\n",
            "  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting pytweening>=1.0.4 (from pyautogui)\n",
            "  Downloading pytweening-1.2.0.tar.gz (171 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m171.2/171.2 kB\u001b[0m \u001b[31m13.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting pyscreeze>=0.1.21 (from pyautogui)\n",
            "  Downloading pyscreeze-1.0.1.tar.gz (27 kB)\n",
            "  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting pygetwindow>=0.0.5 (from pyautogui)\n",
            "  Downloading PyGetWindow-0.0.9.tar.gz (9.7 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting mouseinfo (from pyautogui)\n",
            "  Downloading MouseInfo-0.1.3.tar.gz (10 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting pyrect (from pygetwindow>=0.0.5->pyautogui)\n",
            "  Downloading PyRect-0.2.0.tar.gz (17 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: Pillow>=9.3.0 in /usr/local/lib/python3.11/dist-packages (from pyscreeze>=0.1.21->pyautogui) (11.2.1)\n",
            "Requirement already satisfied: pyperclip in /usr/local/lib/python3.11/dist-packages (from mouseinfo->pyautogui) (1.9.0)\n",
            "Building wheels for collected packages: pyautogui, pygetwindow, pyscreeze, pytweening, mouseinfo, pymsgbox, python3-Xlib, pyrect\n",
            "  Building wheel for pyautogui (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyautogui: filename=pyautogui-0.9.54-py3-none-any.whl size=37682 sha256=a19ccfc23fb6f5e1c9770d0fe1eefb15ab88623e459a90e3a630172e2a661b02\n",
            "  Stored in directory: /root/.cache/pip/wheels/95/dc/b1/fe122b791e0db8bf439a0e6e1d2628e48f10bf430cae13521b\n",
            "  Building wheel for pygetwindow (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pygetwindow: filename=PyGetWindow-0.0.9-py3-none-any.whl size=11063 sha256=2544fd4963ca2e20afda6baea193a474bb20ea8e863cd7dd9da629e8aa90f1be\n",
            "  Stored in directory: /root/.cache/pip/wheels/07/75/0b/7ca0b598eb4c21d43ba4bcc78a0538dfcf803a5997da33bc19\n",
            "  Building wheel for pyscreeze (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyscreeze: filename=pyscreeze-1.0.1-py3-none-any.whl size=14458 sha256=e3ee6e47ffe6d05569f5f7f02e0aa2b86cd3e9f09c340dabb3d889fb201a1813\n",
            "  Stored in directory: /root/.cache/pip/wheels/cd/e3/dd/267b393d8e8f607e47194942740d080d9bfd835cd4375a3de1\n",
            "  Building wheel for pytweening (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pytweening: filename=pytweening-1.2.0-py3-none-any.whl size=8009 sha256=0fba72d9beb1ac0eea16fafea467580a91f8afdef68f5f3148e8e5ecf39b0d6c\n",
            "  Stored in directory: /root/.cache/pip/wheels/db/81/dc/0d61a3c9614f288e057ab63924e2a49edbeed4ffc916dcda1e\n",
            "  Building wheel for mouseinfo (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for mouseinfo: filename=MouseInfo-0.1.3-py3-none-any.whl size=10888 sha256=53af1d68aec3856e43069cc2da536b49fc79d0fa451c30465be0c199e8deb6be\n",
            "  Stored in directory: /root/.cache/pip/wheels/20/0b/7f/939ac9ff785b09951c706150537572c00123412f260a6024f3\n",
            "  Building wheel for pymsgbox (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pymsgbox: filename=pymsgbox-1.0.9-py3-none-any.whl size=7452 sha256=6c944270f5376e26defc81f55e4f8a86a511b9e01052dc97bc409c904bec4fda\n",
            "  Stored in directory: /root/.cache/pip/wheels/85/92/63/e126ee5f33d8f2ed04f96e43ef5df7270a2f331848752e8662\n",
            "  Building wheel for python3-Xlib (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for python3-Xlib: filename=python3_xlib-0.15-py3-none-any.whl size=109501 sha256=13622fa754245155bc7456b8e12770296d3f9905accef36b176b0025f3eefadf\n",
            "  Stored in directory: /root/.cache/pip/wheels/58/d2/1b/c2247396a6c5fbb1900ccf1ec3b73482d428b137dcdf1d99de\n",
            "  Building wheel for pyrect (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyrect: filename=PyRect-0.2.0-py2.py3-none-any.whl size=11181 sha256=5a4037bd8b5c3232d9dbc9e8d32715cbf5beb6ff146b08a778de72eb9e9f0a0b\n",
            "  Stored in directory: /root/.cache/pip/wheels/c4/e9/fc/b7a666dd4f9a3168fb44d643079b41d36ddab52f470707e820\n",
            "Successfully built pyautogui pygetwindow pyscreeze pytweening mouseinfo pymsgbox python3-Xlib pyrect\n",
            "Installing collected packages: pytweening, python3-Xlib, pyrect, pymsgbox, pyscreeze, pygetwindow, mouseinfo, pyautogui\n",
            "Successfully installed mouseinfo-0.1.3 pyautogui-0.9.54 pygetwindow-0.0.9 pymsgbox-1.0.9 pyrect-0.2.0 pyscreeze-1.0.1 python3-Xlib-0.15 pytweening-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pyautogui as pg\n",
        "import time\n",
        "time.sleep(8)\n",
        "\n",
        "for i in range(143):\n",
        "  pg.write(\"i love you\")\n",
        "  pg.press('enter')\n",
        "  pg.write(\"please be okay now..\")\n",
        "  pg.press('enter')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "VfEu7gAMWJiA",
        "outputId": "466141b4-26c1-479f-db79-307aa1cdccef"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "'DISPLAY'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-13-0c2b459d94d6>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mpyautogui\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpg\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m143\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pyautogui/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m    244\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    245\u001b[0m \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 246\u001b[0;31m     \u001b[0;32mimport\u001b[0m \u001b[0mmouseinfo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    247\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    248\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mmouseInfo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/mouseinfo/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m    221\u001b[0m             \u001b[0;32mraise\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    222\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 223\u001b[0;31m     \u001b[0m_display\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mDisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menviron\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'DISPLAY'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    224\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    225\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_linuxPosition\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.11/os.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: 'DISPLAY'"
          ]
        }
      ]
    }
  ]
}