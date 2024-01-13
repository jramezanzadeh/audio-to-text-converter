# audio-to-text-converter
A Python script that renames audio files based on the content.

## Introduction
This script is designed to simplify the process of organizing audio files associated with a textbook by extracting relevant information from the file content and updating file names accordingly.

## Motivation :)
My English teacher was teaching me a book which had many audio files. File names were as follow.
```
├── CD1
│   ├── 01 Track 1.mp3
│   ├── 02 Track 2.mp3
│   ├── 03 Track 3.mp3
│   ├── 04 Track 4.mp3
│   ├── 05 Track 5.mp3
│   ├── 06 Track 6.mp3
│   ├── 07 Track 7.mp3
│   ├── 08 Track 8.mp3
│   ├── 09 Track 9.mp3
│   ├── 10 Track 10.mp3
│   ├── 11 Track 11.mp3
│   ├── 12 Track 12.mp3
│   ├── 13 Track 13.mp3
│   ├── 14 Track 14.mp3
│   ├── 15 Track 15.mp3
│   ├── 16 Track 16.mp3
│   ├── 17 Track 17.mp3
│   ├── 18 Track 18.mp3
│   ├── 19 Track 19.mp3
│   ├── 20 Track 20.mp3
│   ├── 21 Track 21.mp3
│   ├── 22 Track 22.mp3
│   ├── 23 Track 23.mp3
│   ├── 24 Track 24.mp3
│   ├── 25 Track 25.mp3
│   ├── 26 Track 26.mp3
│   └── 27 Track 27.mp3
├── CD2
│   ├── 01 Track 1.mp3
│   ├── 02 Track 2.mp3
│   ├── 03 Track 3.mp3
│   ├── 04 Track 4.mp3
│   ├── 05 Track 5.mp3
│   ├── 06 Track 6.mp3
│   ├── 07 Track 7.mp3
│   ├── 08 Track 8.mp3
│   ├── 09 Track 9.mp3
│   ├── 10 Track 10.mp3
│   ├── 11 Track 11.mp3
│   ├── 12 Track 12.mp3
│   ├── 13 Track 13.mp3
│   ├── 14 Track 14.mp3
│   ├── 15 Track 15.mp3
│   ├── 16 Track 16.mp3
│   ├── 17 Track 17.mp3
│   ├── 18 Track 18.mp3
│   ├── 19 Track 19.mp3
│   ├── 20 Track 20.mp3
│   ├── 21 Track 21.mp3
│   ├── 22 Track 22.mp3
│   ├── 23 Track 23.mp3
│   ├── 24 Track 24.mp3
│   ├── 25 Track 25.mp3
│   ├── 26 Track 26.mp3
│   ├── 27 Track 27.mp3
│   ├── 28 Track 28.mp3
│   └── 29 Track 29.mp3
└── CD3
    ├── 01 Track 1.mp3
    ├── 02 Track 2.mp3
    ├── 03 Track 3.mp3
    ├── 04 Track 4.mp3
    ├── 05 Track 5.mp3
    ├── 06 Track 6.mp3
    ├── 07 Track 7.mp3
    ├── 08 Track 8.mp3
    ├── 09 Track 9.mp3
    ├── 10 Track 10.mp3
    ├── 11 Track 11.mp3
    ├── 12 Track 12.mp3
    └── 13 Track 13.mp3
```
There was neither any information, such as a page number, in the file names, nor any information about the file name in the textbook. However, there was some information, such as the page number and exercise type, inside the files. So, there was no choice but to listen to all the files and figure out which one is the one you want.

It always took quite a long time to find the associated file. That's why I decided to write this script with the help of ChatGPT.

File names after executing this script:
```
├── CD1
│   ├── 01 Track 1.mp3
│   ├── 02 Track 2.mp3
│   ├── 14 Track 14.mp3
│   ├── page_10_exrecise_B
│   ├── page_11_exrecise_F
│   ├── page_13_exrecise_A
│   ├── page_15_exrecise_D
│   ├── page_16_exrecise_A
│   ├── page_18_exrecise_A
│   ├── page_18_exrecise_B
│   ├── page_19_exrecise_A
│   ├── page_19_exrecise_B
│   ├── page_20_exrecise_A
│   ├── page_20_exrecise_C
│   ├── page_22_exrecise_B
│   ├── page_22_exrecise_C
│   ├── page_22_exrecise_D
│   ├── page_23_exrecise_F
│   ├── page_25_exrecise_A
│   ├── page_4_exrecise_A
│   ├── page_5_exrecise_A
│   ├── page_5_exrecise_B
│   ├── page_5_exrecise_D
│   ├── page_6_exrecise_A
│   ├── page_6_exrecise_C
│   ├── page_8_exrecise_B
│   └── page_8_exrecise_C
├── CD2
│   ├── 01 Track 1.mp3
│   ├── 15 Track 15.mp3
│   ├── page_27_exrecise_D
│   ├── page_28_exrecise_A
│   ├── page_28_exrecise_B
│   ├── page_28_exrecise_C
│   ├── page_29_exrecise_A
│   ├── page_29_exrecise_B
│   ├── page_30_exrecise_A
│   ├── page_32_exrecise_A
│   ├── page_33_exrecise_C
│   ├── page_33_exrecise_D
│   ├── page_33_exrecise_E
│   ├── page_34_exrecise_B
│   ├── page_37_exrecise_A
│   ├── page_39_exrecise_D
│   ├── page_40
│   ├── page_40_exrecise_A
│   ├── page_40_exrecise_B
│   ├── page_41_exrecise_A
│   ├── page_41_exrecise_B
│   ├── page_42_exrecise_A
│   ├── page_44_exrecise_B
│   ├── page_46_exrecise_A
│   ├── page_46_exrecise_C
│   ├── page_47_exrecise_D
│   ├── page_47_exrecise_E
│   └── page_49_exrecise_A
└── CD3
    ├── 01 Track 1.mp3
    ├── page_51_exrecise_D
    ├── page_52_exrecise_A
    ├── page_53
    ├── page_53_exrecise_B
    ├── page_54_exrecise_A
    ├── page_56_exrecise_B
    ├── page_58_exrecise_A
    ├── page_58_exrecise_C
    ├── page_58_exrecise_D
    ├── page_59_exrecise_E
    └── page_61_exrecise_A
```

## Requiremnets
Ensure the following packages are installed.
```bash
sudo apt-get install ffmpeg
pip install SpeechRecognition pydub
```
## Usage
To use the script, you can pass a directory containing audio files or provide a list of files as input argumnet.

If both the `-f` and `-d` options are provided, the script will use the `-f` option, and the `-d` option will not be considered.

### Examples
```bash
python3 rename_audio_files.py -d audi_files/

python3 rename_audio_files.py -f audio_files/01\ Track\ 1.mp3 audio_files/02\ Track\ 2.mp3 audio_files/06\ Track\ 6.mp3
```

## Customization
Feel free to customize the script according to your needs. You most likely need to adapt the `pattern_string` variable and the `extract_page_number_and_excercise_type` function to derive your appropriate file name from the file content.