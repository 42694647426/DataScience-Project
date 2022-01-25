# Analysis of tweets regarding Covid 19 situation
The project focus on the analysis of the tweets concerning the current Covid 19 situation in a 3-days window. The collected posts will be cleaned (elimininate invalid data) and classified into 5 categories listed below and labeled with the sentiment. A stream of analysis was performed and the results were embedded into the report. 

# Topic Category
3~8 Topics

### O: Omicron
Including mention about "new variant", Delta, etc.

### V: Vaccine 
(anything related to vaccine, including vaccine passport, child vaccine)

### N: News 
(including mention some famous people, which famous test postivie, new policies etc.)

### I: Influences 
About something really happened.
(experience, symptoms, daily life, lose job, what people do or change during covid perioed)

### P: Opinion comments 
Something maybe not happen. i.e. not facts.
Including emotional comments and opinions about Covid, ironic comments, doubt comments, questions, concerns.

("I don't want to die" "I hate getting tested" "Covid will live with us forever" "@xxx have you ever consider xxx?")

### Categorized priority from top to down. 

e.g.: If you find one tweet can be categorized as both
"V" and "N", denoted it as "V".


# Sentiment Category
positive/neutral/negative

### P: Positive

### E: Neutral

### N: Negative

# Running Scripts Instructions

```bash
python ./src/categorize.py  # this creates a tsv file in /data directory with simple annotations done by python.  
```

