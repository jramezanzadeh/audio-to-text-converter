import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import os
import re
import argparse
import sys

pattern_string = r'.*(?:page (\d+))(?:.*exercise ([a-zA-Z]))?'

def extract_page_number_and_excercise_type(text):
    pattern = re.compile(pattern_string)
    matches = pattern.match(text)

    if matches:
        page_number = matches.group(1)
        exercise_type = matches.group(2) if matches.group(2) else None 
        return page_number, exercise_type
    else:
        return None, None

def rename_file(current_filename, new_filename):
    try:
        os.rename(current_filename, new_filename)
        print(f"File successfully renamed from '{current_filename}' to '{new_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{current_filename}' not found.")
    except FileExistsError:
        print(f"Error: File '{new_filename}' already exists.")
    
def list_files_recursively(directory_path):
    file_list = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

def convert_mp3_to_text(mp3_file_path):
    # Load MP3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Export MP3 as WAV (temporary file)
    wav_file_path = "temp.wav"
    audio.export(wav_file_path, format="wav")

    # Perform transcription on the converted WAV file
    text = convert_wave_to_text(wav_file_path)

    return text

def convert_wave_to_text(wav_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file_path) as source:
        # Adjust for ambient noise
        # recognizer.adjust_for_ambient_noise(source)

        # Listen to the audio file
        audio = recognizer.record(source, duration=10)

    try:
        # Use Google Web Speech API to recognize the speech
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the request to Google Web Speech API: {e}")

if __name__ == "__main__":
    # Process input arguments
    parser = argparse.ArgumentParser(description="Rename audio files based on their content.")
    parser.add_argument('-f', '--files', nargs='+', help='List of file names to rename. In case of providing both -f and -d options, -f is given higher preference')
    parser.add_argument('-d', '--files-dictionary', nargs=1, help='Dictionary including files to rename. Directory is searched recursively')
    args = parser.parse_args()

    if not args.files and not args.files_dictionary:
        parser.error('At least one of the options -f or -d is required.')
    
    # Extract list of files
    if args.files_dictionary:
        file_list = list_files_recursively(args.files_dictionary[0])
    
    if args.files:
        file_list = args.files
    
    if not file_list:
        parser.error('List of files is empty.')
    
    # Rename Files
    for file in file_list:
        result = convert_mp3_to_text(file)
        print("old file:", file)
        page_number, exercise_type = extract_page_number_and_excercise_type(result.lower())
        if page_number is not None:
            # print("page_" + page_number)
            new_file_name = "page_" + page_number 
            if exercise_type:
                new_file_name += "_exrecise_" + exercise_type.upper() 
            file_dir, old_file_name = os.path.split(file)
            new_file = file_dir + "/" + new_file_name
            print("new_file:", new_file)
            rename_file(file, new_file)
        else:
            print(f"Couldn't find pattern '{pattern_string}' in the file content '{result}'")
            # print(result)
        print("**********************************\n\n")
    if os.path.exists("temp.wav"):
        os.remove("temp.wav") # Better to handle exceptions

