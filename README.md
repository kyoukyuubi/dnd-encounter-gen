# Dungeons & Dragons Encounter Generator

This CLI project will generate a random encounter based on parameters parsed to it. Like what level and what size the party is, it can even generate multiple enemies, or just one.
It is generating the counters based on the Experience budget presented in the Dungeons Masters Guide 2024, in **Chapter 4: Creating Adventures** under **Combat Encounters**->**Combat Encounter Difficulty**->**XP Budget per Character**. 

## How to use

It is really simple to use, you run the run.sh file and parse in the options you want. You can use `--help` or `--h` to see all options avaiable! They are all optional.

**Example**
`./run.sh --level 15 --size 5 --min_exp 23500 --max_creatures 1`
This would generate a boss fight! Here is the output:

Encounter Generated!
------------------------------
Name: Leviathan
Amount: 1
Challenge Rating: 20
Environment: Underwater, Coastal
The creature can be found in: Mordenkainen's Tome of Foes on page: 198


## Adding more creatures

Currently this project holds 29 creatures from 2 books, they are located in the data folder. All you need to do is edit the .json files inside to add more creatures! Currently each file represents a book.
To add a new book, just make a new .json file and call it what you what, I'd recommend you abbreviate the book name and add _creatures after it. For example, for the book Volo’s Guide to Monsters. I would name it: 
> vgtm_creatures.json.

Here is the formatting needed in the .json files. I am using the `Aboleth` and `Beholder` from  `Monster Manual 2024` to show how you add multiple creatures:

```json
{
    "Creatures": [
      {
        "Name": "Aboleth",
        "Type": "Aberration",
        "ChallengeRating": "10",
        "Exp": 5900,
        "Environment": ["Underwater"],
        "Plane": [],
        "Book": "Monster Manual 2024",
        "Page": "12"
      },
      {
        "Name": "Beholder",
        "Type": "Aberration",
        "ChallengeRating": "13",
        "Exp": 10000,
        "Environment": ["Underdark"],
        "Plane": [],
        "Book": "Monster Manual 2024",
        "Page": "36"
      }
    ]
  }
```
You don't have to add multiple, I am just showing how!
