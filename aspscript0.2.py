"""
Version Summaries
0.2 Plan: Plans to rewrite the script
"""
import os
from pathlib import Path
import time
import math
import datetime
from typing import ContextManager, Counter

instructions = {
    "001 Welcome to the Data pack setup instructions! This is not in order.",
    "002 i uh- hopefully this will be automatic one day.",
    "003 So first, make a folder that will be the data pack 'root folder'. I'll be calling this root"
}

file1 = open('subscript.txt', 'r')
Lines = file1.readlines()

# Data pack setting holders
packformat = "insert"
description = "insert"
jsonname = "null"


importantcyclekeep = 0
contextclue = 0
valuesearch = 0
multilinesearch = 0
valueparticle = "Six"
scanner = 1
directoryname = "null"
infolder = "null"
previousdir = "null"

"""
Alright, so with Important Cycle Keep
This variable will be checked upon line read for information needed!
Here are it's values and what they mean

0: Null
1: Initialise Minecraft was called upon
2: First Setting was called
3: Post Minecraft Search
4: Looking for directory
5: Multi-line search for json
6: Multi-line search for biome
7: Value Adding

And Context Clue
Context clue is used for multi use points such as 'Settings {'
Here are what the context clue values mean:

0: Null
1: Looking for Initialise Settings
2: Directory created

Value Search
This is so Minescript can point out individual floats in a script

0: Null
1: PackFormat
2: Description
3: Make Folder
4: Make World Gen Folder
5: Finding Make script
6: Finding the name of JSON
7: Finding the extensive float for functions or other files of such nature
8: Finding name of biome
9: Finding extensive float for biome or other files of such nature

Multi line search
When Multi line search is set, Minescript ignores everything else that might need to be called in favour of generating a text file.

0: Null
0<: Active

Directory Name
Directory name is mainly to help the instructions dictate how things should run.

Null: Shouldn't appear unless people have an explicit reason.
Other: This is the name of folder
"""
linecheck = 0

currentdate = datetime.datetime.now()
print(currentdate)

logfile = open('MinescriptLog.txt', 'a')

packmeta = open('pack.mcmeta', 'r+')

# Generate Log
def GenerateLog():
    logfile.write("""
    The current date is {}
-------------------------------

    Aspiron Logs - This is for Minescript

-------------------------------
    Okay- Hey! It is I- the log person
    Right so i'll assist you in going through this log. cause i'm unique that way!

    First lets take a look at the variables that Minescript has upon this getting called

Right so, The date is,
{}
If it's incorrect, either scroll down or check ur computer time.
The Rememberance values, are:
{} - Important Cycle Keep
{} - Context Clue
{} - Value Search
{} - Multi Line Search

    Right! So lets take a look at variables:
{}
{}

{}
{}
{}

{}
{}
{}
{}

{}
{}
{}
{}
{}

{}
{}
{}
{}
{}
{}

    Now, Lets take a look at the text files that needed to be generated:
    If smth says null- it either wasn't used- or the program failed to write it

    // Pack.mcmeta
Format Version:
{}
Description:
{}

    Now you'll probably want the instructions for how to get this to work as a data pack!
    Lets here is the best tutorial:
    (!) remember that the tutorial is generated by the code itself. This won't always give the best help. if you have any confusion, bring it to discord (!)

    {}

""".format(currentdate, currentdate, importantcyclekeep, contextclue, valuesearch, multilinesearch, Two1, Two2, Three1, Three2, Three3, Four1, Four2, Four3, Four4, Five1, Five2, Five3, Five4, Five5, Six1, Six2, Six3, Six4, Six5, Six6, packformat, description, instructions))

rootfolder = Path("/Aspiron/Minescript/Export/DATAPACK").mkdir(parents=True, exist_ok=True)

instruction = 4
jsonping = open('dontincludethis.txt', 'a')

# Value setup
"""
2 Way Value

Usage: None
"""
Two1 = 0
Two2 = 0
"""
3 Way Value

Usage: None
"""
Three1 = 0
Three2 = 0
Three3 = 0
"""
4 Way Value

Usage: None
"""
Four1 = 0
Four2 = 0
Four3 = 0
Four4 = 0
"""
5 Way Value

Usage: None
"""
Five1 = 0
Five2 = 0
Five3 = 0
Five4 = 0
Five5 = 0
"""
6 Way Value

Usage: None
"""
Six1 = 0
Six2 = 0
Six3 = 0
Six4 = 0
Six5 = 0
Six6 = 0

# Strips the newline character
for line in Lines:
    linecheck += 1
    print("Read: {}".format(line.strip()))
    if (line.strip()) == 'MineSetup:':
        print("Action: Initialise has been called for a Minecraft Data pack")
        importantcyclekeep = 1
        contextclue = 1
    if importantcyclekeep == 1:
        if (line.strip()) == 'Settings:' and contextclue == 1:
            print("Action: Settings has been called")
            importantcyclekeep = 2
    if (line.strip()) == 'Set 6-Way Value:':
        valueparticle = "Six"
        multilinesearch = 6
        importantcyclekeep = 7
        scanner = 1
    if (line.strip()) == 'InDirectory:':
        print("Action: Minecraft has been found")
        instructions.add("00{} Make a folder titled data in the root folder. (root/data)".format(instruction))
        instruction += 1
        importantcyclekeep = 3
    if multilinesearch > 0:
        if importantcyclekeep == 5:
            jsonping.write("    {}\n".format(line.strip()))
            multilinesearch -= 1
        if importantcyclekeep == 7:
            if scanner == 1:
                Six1 = line.strip()
            if scanner == 2:
                Six2 = line.strip()
            if scanner == 3:
                Six3 = line.strip()
            if scanner == 4:
                Six4 = line.strip()
            if scanner == 5:
                Six5 = line.strip()
            if scanner == 6:
                Six6 = line.strip()
            multilinesearch -= 1
            scanner += 1
    #in file
    if valuesearch == 7:
        print("Action: Right. now for the hard stuff. Turn the next (x) amount of lines into a json")
        multilinesearch = int(line.strip())
        instructions.add("""00{} Move the json file named '{}' into (root/data/{}/{})""".format(instruction, jsonname, previousdir, infolder))
        jsonping = open('{}.json'.format(jsonname), 'a')
        valuesearch = 0
    if (line.strip()) == 'InFile[':
        if valuesearch == 6:
          print("Action: Searching for contents of a file now.")
          valuesearch = 7
          importantcyclekeep = 5
    if (line.strip()) == 'InFile[':
        if valuesearch == 8:
            print("Action: Searching for contents of a biome file now.")
            valuesearch = 9
            importantcyclekeep = 6
    #Finding Directory Name
    if importantcyclekeep == 4:
        if contextclue == 2:
            print("Action: Found Directory name")
            directoryname = line.strip()
            instructions.add("""00{} Make a folder titled {} in the data folder. (root/data/{})""".format(instruction, directoryname, directoryname))
            previousdir = directoryname
            instruction += 1
            contextclue = 0
            importantcyclekeep = 0
            valuesearch = 0
    if importantcyclekeep == 3:
        if (line.strip()) == 'Settings:' and contextclue == 2:
            print("Action: Directory settings found")
            importantcyclekeep = 4
    #Make JSON
    if valuesearch == 6:
        print("Action: better have found the json name")
        jsonname = line.strip()
        print(jsonname)
    if valuesearch == 8:
        print("Action: better have found the biome json name")
        jsonname = line.strip()
        print(jsonname)
    if valuesearch == 5 and line.strip() == "MakeJSON(V)":
        print("Action: Right boys- lets make a json grr")
        valuesearch = 6
    if valuesearch == 5 and line.strip() == "MakeBiome(V)":
        print("Action: Right boys- lets make a biome grr")
        valuesearch = 8
    #Make Folder
    if valuesearch == 3:
        print("Action: Setting normal folder value")
        directoryname = line.strip()
        instructions.add("""00{} Make a folder titled {} in DIR (root/data/{}/{}*)""".format(instruction, directoryname,previousdir, directoryname))
        instruction += 1
        infolder = directoryname
        valuesearch = 5
    if (line.strip()) == 'MakeFolder:':
        print("Action: Make Folder has been called. Searching for the next value")
        valuesearch = 3
    if valuesearch == 4:
        print("Action: Setting worldgen modified folder value")
        directoryname = line.strip()
        instructions.add("""00{} Make a folder titled worldgen in DIR (root/data/{}/worldgen)""".format(instruction, previousdir))
        instruction += 1
        instructions.add("""00{} Make a folder titled {} in worldgen (root/data/{}/worldgen/{}*)""".format(instruction, directoryname, previousdir, directoryname))
        instruction += 1
        infolder = "worldgen/{}".format(directoryname)
        valuesearch = 5
    if importantcyclekeep == 0:
        if (line.strip()) == 'MakeWorldFolder:':
            print("Action: Make Folder has been called. Searching for the next value")
            valuesearch = 4
    #Directory called
    if importantcyclekeep == 3:
        if (line.strip()) == 'Dir:':
            print("Action: Directory has been called- We now need to get name.")
            contextclue = 2
    if valuesearch == 1:
        packformat = line.strip()
        print("Action: Pack Format has been set")
        valuesearch = 0
    if valuesearch == 2:
        description = line.strip()
        print("Action: Description has been set")
        instructions.add("00{} Grab the pack.mcmeta folder, and copy and paste it into the root folder. (root/pack.mcmeta)".format(instruction))
        packmeta.write(
"""
{
"pack": {
"pack_format": 7,
"description": "SET DESCRIPTION"
}
}
""")
        instruction += 1
        valuesearch = 0
        importantcyclekeep = 0
        contextclue = 0
    if (line.strip()) == 'end':
        print("Action: Minescript has found an end")
        GenerateLog()
    if importantcyclekeep == 2:
        if (line.strip()) == 'pack_format' and contextclue == 1:
            print("Action: Settings has been called")
            importantcyclekeep = 2
            valuesearch = 1
    if importantcyclekeep == 2:
        if (line.strip()) == 'description' and contextclue == 1:
            print("Action: Settings has been called")
            importantcyclekeep = 2
            valuesearch = 2

