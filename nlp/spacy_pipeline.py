import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("We express our gratitude to Stefan Reichelstein, the editor, and the two anonymous reviewers for valuable feedback. We are also thankful to workshop participants at Michigan State, Drexel, Rutgers, and Northwestern University. In particular, we would like to extend our appreciation to James Anderson, Ken Bills, Helen Choy, Elizabeth Connors, Aaron Fritz, Martin Holzhacker, Marilyn Johnson, Ranjani Krishnan, Andrew Leone, Harlow Loch, Ryan McDonough, Wayne Nesbitt, Michelle Nessa, Hari Ramasubramanian, Georg Rickmann, Sugata Roychowdhury, Sri Sridharan, Isabel Wang, and Aaron Yoon for their comments. Finally, Jiang would like to acknowledge the generous research support from the Eli Broad College of Business and the Eli Broad Professorship.")

def process_text(text):
    doc = nlp(text)

    sentences = [sent.text for sent in doc.sents]

    results = []
    for sent in doc.sents:
        results.append({
            "text": sent.text,
            "lemmas": [token.lemma_ for token in sent],
            "pos_tags": [(token.text, token.pos_) for token in sent],
            "entities": [(ent.text, ent.label) for ent in sent.ents]
        })

    return results 

def main():
    process_text(doc)

if __name__ == "__main__":
    main()