<img src="https://gitlab.com/uploads/-/system/project/avatar/12442001/tgthemer_round.png" width="200px">

## Synopsis
A telegram(for android) theme generator written in python (3.7)

## Code example
```python
from tgthemer import Themer

themer = Themer(primary='#FF18181F',  # theme primary colour
                accent='#FFFFF58F',   # theme accent colour
                ttype='dark')         # theme type

themer.generate_android(out="my_fab_theme")
```

## Motivation
Telegram (for android) has got ~500 color variables to edit in order to make a theme. Which is good since it provides maximum customizability, but that makes creating a theme a very tedious process for its users. This module tries to fix it. In fact you only need to specify 2 colors to automatically generate a coherent theme.

## Installation
```bash
# clone the repository
git clone https://gitlab.com/Eskilop/tgthemer esky_tgthemer

# cd into project directory
cd esky_tgthemer

# install
python setup.py install
```

## API reference
#### Themer
The main object of the module, it allows you to generate a new theme by specifying the basic colors to start from.
* \_\_init\_\_(self, primary="FF000000", secondary="FF000000", accent="FF000000",
                 mode=None, ttype="dark")
	* primary (string)<br>the primary color of your theme
	* secondary (string)<br>the secondary color of your theme, if none is passed, it will be generated from primary
	* accent (string)<br>the accent color of your theme, no checks will be done, so you can insert any color here.
	* mode (string)[lighten/darken]<br>specifies how to generate secondary and tertiary colors, by default, a ttype="dark" theme will have a "lighten" mode while a light theme will have "darken" mode.
	* ttype (string)[dark/light]<br>specifies the theme type, which regulates mode
* Properties
	* human_dict (dict)<br>returns a "telegram_color_key": "#FFC0FFEE" dictionary
	* telegram_dict (dict)<br>returns a "telegram_color_key": signed_int_value dictionary
	* telegram_string (string)<br>returns the string representation in the format "tg_color_key=signed_int_value\n"
	* human_string (string)<br>returns the string representation in the format "tg_color_key=#FFC0FFEE"
* Methods
	* generate_android(custom=None, out=None)<br>takes an input file from sources/ depending on which theme type you passed in the constructor and writes the generated theme in "out/"+out+".attheme"

#### Color
Auxiliary class which allows argb colors to be represented. It manages color conversions and alpha channel editing. You need to specify either one of the parameters, if both are specified, the hex value is taken.
* \_\_init\_\_(self, hex=None, sint=None)
	* hex (string)<br>hexadecimal argb value for a color
	* sint (int)<br>signed integer value for a color
* Properties
	* sint (int)<br>signed integer representation of the provided color
	* hex (string)<br>hexadecimal representation of the provided color
	* argb (tuple)<br>(alpha, red, green, blue) representation of provided color
* Methods
	* lighten(percent) (Color)<br>returns a Color lightened by the specified percent (int), note that you can darken a color by specifying a negative value. No checks on percent bounds are made.
	* alpha(percent) (Color)<br>returns a Color with an alpha channel edited by percent (int), you can pass a positive value to increase the alpha channel, a negative one to decrease it. No checks on percent bounds are made.
## Tests
install [pytest](https://docs.pytest.org/en/latest/getting-started.html) then:
```bash
cd esky_tgthemer  # assuming that you cloned and saved it as this

pytest  # execute
```

## License
```
MIT License

Copyright (c) 2019 Eskilop

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```