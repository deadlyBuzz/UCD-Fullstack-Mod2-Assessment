# Readme
This project is to provide a live version of the URC table where the fans can see how the current scores are impacting the table in real time.
Fans enter the scores and the data is added automatically
A Excerpt from the Instructions is shown:

## Introduction
<p>
    I've been there more than once, on the stands of thomond park, at the crunch time in the season and everyone has their calculators and calendars out.
    If we win this, are we through?
    If we win this but Glasgow get a bonus point, what does that mean?
    What is the score in the Leinster match, are they far ahead enough to make a difference?
</p>

<p>
    And it seems, nowhere has the answers.
    Some websites, like BBC or Sky Sports have some live scores but no update to what the table look like.
    Google has all the scores but not a table to tell you the true picture.
    If watching it on TV, SKY Sports may briefly pop up an "as it stands" table subset showing you some information but it's not something you can rely on or count on being there when the questions are asked.</p>
<p>
    This Page is the answer.
</p>
<p>
    It is a community sourced live table predictor with real live data.
    The Community enter the scores for a match as it comes in and the website uses this data, and this data alone to build a set of data that shows the live table based on the given scores.
    Fans can use this website to see how each team is faring in the table and in each match in real time.
</p>

## Instructions
<p>
    On the main landing page, the table is displayed at the top showing what the table looks like today, with which round has been played.<br>
    Beneath the table, there is a list of the matches.
</p>
    To update the match: 
    <ul>
        <li>click the banner of the match.</li>
        <li>This will take you to the Match Page.</li>
        <li>From here, there are two controls above a display of the selected match.</li>
        <li>The Controls on the left are to update the HOME score.</li>
        <li>The Controls on the right are to update the AWAY score.</li>
        <li>When a team has scored, select the score from the dropdown.</li>
        <li>Once you have selected the score that has been scored, the site will add this to the history (shown at the bottom of the card) and the table will be re-calculated with the new statistic</li>
        <li>If you make a mistake, and a score has been added in error, you can select the "undo" button</li>
        <li>This will remove the last score added from the match</li>
        <li>Once you have pressed UNDO, the UNDO button will remain disabled until you add another score.</li>
        <li>Only if you undo a Conversion, will you be able to undo once again to remove the associated try as well</li>
        <li>when finished, just press the HOME button to go back to the main page</li>
    </ul>

# AI Usage
To be fair, I had little use of AI for thsi project, simply some questions on how to iterate through a list of dictionaries, or sort a list of dictionaries when a simple search gave me a very specific (yet irrellevant) result from stack overflow 16 years ago.

# Samples
I reviewed the samples from the course to find what works and reversed engineered them to get this site working.
One key part I found I took a lot though was the contact form.  It did what I needed it to and I was running out of time so this is mostly copied from the samples in the course, credit to **Housam Ziad** for the code.

# Self criticism
This was very much biting off more than i should have tried chewing.  I spent way too long on the actual functionality and have left too little for acessiility and styling.
The code is inconsistent.  I had some places where I looped through a list with a `For Each` statement and then picked out what i wanted, before I found the `next` function.
I had planned to use a more consistent case for capitalisation but this is not the same throughout and is definitely a fallback but I have run out of time to implement this.
I have tried using `.GET(key)` but when getting the logic working, the code `["key"]` worked as well and I didn't get a chance to go back and fix it.

# Accessing
The code and files can be found at this github repo: https://github.com/deadlyBuzz/UCD-Fullstack-Mod2-Assessment
The site is uploaded to render.com at: https://ucd-full-stack-module-2-python-assessment.onrender.com/


