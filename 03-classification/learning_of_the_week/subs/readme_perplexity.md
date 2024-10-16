# Unlocking the Power of ML Zoomcamp: A Subtitle Adventure

Are you ready to supercharge your [ML Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp/) experience? Buckle up, because we're about to embark on a journey that will transform how you engage with the course content!

## The Subtitle Revolution

As a fellow ML Zoomcamp participant, I found myself pondering ways to keep pace with the lectures. Then it hit me – what if we could harness the power of subtitles? Imagine being able to:

- Read lectures at your own pace
- Seamlessly integrate content into your notes
- Make lectures text-searchable
- Feed subtitles to our trusty Slack `@ZoomcampQABot` for instant answers

Sounds amazing, right? Let's dive in and make this a reality!

## Your Subtitle Toolkit: yt-dlp

First things first, we need a powerful ally. Enter [yt-dlp](https://github.com/yt-dlp/yt-dlp), our subtitle-downloading superhero!

### Installation

Choose your fighter:

Linux warriors:
```bash
pip install yt-dlp
```

macOS aficionados:
```bash
brew install yt-dlp
```

## Preparing for Battle

Let's create our subtitle sanctuary:

```bash
mkdir subs
cd subs
```

## Reconnaissance: Scouting for Subtitles

Before we dive in, let's see what we're up against:

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=Jt2dDLSlBng&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
```

Spoiler alert: We're dealing with auto-generated subtitles. Challenge accepted!

## The Great Subtitle Heist

Time to acquire our precious subtitle treasure:

```bash
yt-dlp \
--write-auto-subs \
--skip-download \
--sub-lang en \
"https://www.youtube.com/watch?v=Jt2dDLSlBnglist=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
```

## Subtitle Makeover: From Messy to Marvelous

Our subtitles need a spa day. Let's enlist the help of our AI friend, ChatGPT, for some serious pampering!

After some back-and-forth with our AI stylist, we've got two fabulous Python scripts:

1. [clean_subs.py](./src/clean_subs.py) - The basic cleanse
2. [clean_subs_10xline.py](./src/clean_subs_10xline.py) - The deluxe treatment

Run them like a boss:

```bash
python clean_subs.py
python clean_subs_10xline.py
```

## Manual Mode: When Automation Needs a Human Touch

For those rebellious Q&A sessions, we're going old school:

```bash
yt-dlp \
--write-auto-subs \
--skip-download \
--sub-lang en \
"https://www.youtube.com/live/MqI8vt3-cag?si=TuTo5C9HXIClcNHZ"
```

## The Audio Whisperer: Buzz to the Rescue

When YouTube's transcription falls short, we call in the big guns: [Buzz](https://chidiwilliams.github.io/buzz/docs "Buzz documentation")!

```bash
brew install --cask buzz
```

Buzz works its magic, turning audio into beautiful .txt, .srt, and .vtt files.

## The Grand Finale

We did it! We've transformed raw subtitles into a learning powerhouse. But this is just the beginning. Our friendly @ZoomcampQABot is chomping at the bit to devour these subtitles and become even more helpful.

And guess what? The mastermind behind ML Zoomcamp, Alexey Grigorev, is on board with our subtitle revolution. We're working on integrating these gems into @ZoomcampQABot as we speak.

So, fellow ML enthusiasts, get ready for a learning experience like no other. With our subtitle superpowers, we're not just keeping pace – we're setting the pace!

Stay tuned for more updates, and happy learning!

Citations:
[1]: 