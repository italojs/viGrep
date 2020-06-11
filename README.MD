# ViGrep
It's a cli to extract text from video by a regex.

# Index :book:

- [How it works?](#How-it-works?)
- [Dependencies](#Dependencies)
- [Install python requirements](#Install-python-requirements)
- [Usage](#Usage)
- [Example](Example)
- [Output](Output)

### How it works? :gear:
- Excecute the cli informing your file
- Get the matched words separeted by video seconds in a output.txt file
- Be happy

## Dependencies :warning:
We are using tesseract, it's a free open source Google's OCR, you must install it in your system before continue.

[Tesseract installation instructions](https://tesseract-ocr.github.io/tessdoc/Home.html)

## Install python requirements :construction:
```
pip install -r requirements.txt
```

## Usage :clapper:
`python main.py -h`

```
usage: main.py [-h] [-i INPUT] [-r [REGEX]] [-o OUTPUT] [-v VERBOSE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path to input video file
  -r [REGEX], --regex [REGEX]
                        regex to find text in video frames
  -o OUTPUT, --output OUTPUT
                        path to (optional) output video file
  -v VERBOSE, --verbose VERBOSE
                        If 1(True) will be printed in output file the text
                        used in regex
```

## Example :eyes:
```
python main.py --input "video.mkv" --regex "((https?:\/\/(www)?)?[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,})" --verbose 1
```

## Output :hankey:

### Verbose disabled
```
frame: 1 | second: 0.001 | matches: [('stackoverflow.com/quest', '', '')]
frame: 2 | second: 0.031 | matches: [('stackoverflow.com/questions', '', '')]
frame: 3 | second: 0.064 | matches: [('stackoverflow.com/questions', '', '')]
frame: 4 | second: 0.096 | matches: [('stackoverflow.com/questions', '', '')]
```


### Verbose enabled
```
 text: <text extracted by tessaract in the current frame>
frame: 1 | second: 0.001 | matches: [('stackoverflow.com/quest', '', '')]
-------------------------------------------------- 

 text: <text extracted by tessaract in the current frame> 
frame: 2 | second: 0.031 | matches: [('stackoverflow.com/questions', '', '')]
-------------------------------------------------- 

 text: <text extracted by tessaract in the current frame>
frame: 3 | second: 0.064 | matches: [('stackoverflow.com/questions', '', '')]
```