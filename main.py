import streamlit as st
import sqlite3
import os
import random

# Configuration des bases de données
DB_NAME_SCORES = "qcm_scores.db"
DB_NAME_QUESTIONS = "qcm_questions.db"

def init_dbs():
    """Initialise les bases de données pour stocker les scores et les questions si elles n'existent pas."""
    # Vérification pour la base de données des scores
    if not os.path.exists(DB_NAME_SCORES):
        conn_scores = sqlite3.connect(DB_NAME_SCORES)
        cursor_scores = conn_scores.cursor()
        cursor_scores.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
        conn_scores.commit()
        conn_scores.close()

    # Vérification pour la base de données des questions
    if not os.path.exists(DB_NAME_QUESTIONS):
        conn_questions = sqlite3.connect(DB_NAME_QUESTIONS)
        cursor_questions = conn_questions.cursor()
        cursor_questions.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer TEXT NOT NULL
            )
        """)
        conn_questions.commit()
        conn_questions.close()

def questions_exist():
    """Vérifie si des questions existent déjà dans la base de données."""
    conn = sqlite3.connect(DB_NAME_QUESTIONS)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM questions")
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def add_questions_to_db():
    """Ajoute des questions et réponses à la base de données uniquement si elles n'existent pas."""
    if questions_exist():
        st.warning("Les questions existent déjà dans la base de données. Aucun ajout nécessaire.")
        return
    
    questions = [
        # Questions existantes
        ("Qui a défini le management comme la mise en œuvre de moyens humains pour atteindre des objectifs communs ?", 
         "F. Dupuy", "P. Drucker", "A. Mehrabian", "Bateson", "P. Drucker"),
        ("Le management participatif est :", 
         "Très organisationnel, peu relationnel", "Très relationnel, peu organisationnel", 
         "Peu organisationnel et relationnel", "Très organisationnel et relationnel", 
         "Très relationnel, peu organisationnel"),
        ("L’homéostasie dans l’approche systémique correspond à :", 
         "La capacité à produire des résultats communs", "La résistance au changement d’un système", 
         "Une méthode de communication non verbale", "La collaboration entre équipes", 
         "La résistance au changement d’un système"),
        ("Dans le modèle de Mehrabian, quel pourcentage est attribué aux mots dans la communication ?", 
         "7%", "38%", "55%", "60%", "7%"),
        ("Quel type de management convient le mieux à des collaborateurs expérimentés ?", 
         "Directif", "Participatif", "Délégatif", "Persuasif", "Délégatif"),

        # Questions enrichies
        ("Quel est le principal objectif du management directif ?", 
         "Encourager la prise d'initiative", "Fournir des instructions claires", 
         "Renforcer les compétences des employés", "Permettre l'autonomie", 
         "Fournir des instructions claires"),
        
        ("Le management participatif vise principalement à :", 
         "Renforcer l’autorité du manager", "Favoriser la collaboration des employés", 
         "Imposer des décisions top-down", "Diminuer les coûts de production", 
         "Favoriser la collaboration des employés"),
        
        ("Dans quelle situation un management délégatif est-il le plus adapté ?", 
         "En cas de crise", "Avec des collaborateurs expérimentés", 
         "Lorsque la communication est défaillante", "Pour imposer des tâches précises", 
         "Avec des collaborateurs expérimentés"),
        
        ("Quel type de management est caractérisé par une approche 'laissez-faire' ?",
         "Participatif", "Délégatif", "Directif", "Persuasif", 
         "Délégatif"),
        
        ("Le changement dans une organisation est souvent perçu comme une source de :", 
         "Stabilité", "Risque", "Innovation", "Conformité", 
         "Risque"),
        
        ("Une des clés de la gestion des conflits selon l’approche systémique est :",
         "Ignorer les causes sous-jacentes", "Comprendre les logiques des individus", 
         "Imposer une solution autoritaire", "Réduire la communication", 
         "Comprendre les logiques des individus"),
        
        ("Dans l’approche systémique, l’homéostasie fait référence à :", 
         "La capacité d'un système à maintenir son équilibre", 
         "Le désir de changement", "La résistance aux décisions extérieures", 
         "La collaboration entre départements", 
         "La capacité d'un système à maintenir son équilibre"),
        
        ("Le leader et le manager diffèrent par :", 
         "Le leader est désigné, le manager est reconnu", "Le leader inspire, le manager dirige", 
         "Le manager est plus influent que le leader", "Le manager est créatif, le leader est autoritaire", 
         "Le leader inspire, le manager dirige"),
        
        ("Lors d’un conflit, une des premières actions à mener est :",
         "Faire preuve de neutralité et écouter chaque partie", "Imposer une solution rapide", 
         "Ignorer les émotions", "Accuser la partie fautive", 
         "Faire preuve de neutralité et écouter chaque partie"),
        
        ("Dans une organisation, quel type de management favorise l’autonomie des collaborateurs ?", 
         "Participatif", "Directif", "Délégatif", "Persuasif", 
         "Délégatif"),
        
        ("Le processus de changement est généralement plus facile à gérer dans :", 
         "Un environnement complexe", "Un environnement stable", 
         "Un environnement rigide", "Un environnement simple", 
         "Un environnement complexe"),
        
        ("Le principal facteur de réussite d’un changement est :", 
         "La résistance des collaborateurs", "L’implication émotionnelle", 
         "L’autorité du manager", "La suppression des obstacles", 
         "L’implication émotionnelle")
    ]
    
    conn = sqlite3.connect(DB_NAME_QUESTIONS)
    cursor = conn.cursor()
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, q)
    conn.commit()
    conn.close()
    st.success("Questions ajoutées avec succès à la base de données.")

    ]
    conn = sqlite3.connect(DB_NAME_QUESTIONS)
    cursor = conn.cursor()
    for q in questions:
        cursor.execute("""
            INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, q)
    conn.commit()
    conn.close()
    st.success("Questions ajoutées avec succès à la base de données.")

def add_score(name, score):
    """Ajoute un score à la base de données."""
    conn = sqlite3.connect(DB_NAME_SCORES)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def get_best_score():
    """Récupère le meilleur score enregistré."""
    conn = sqlite3.connect(DB_NAME_SCORES)
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result if result else ("Aucun", 0)

def get_random_questions():
    """Récupère 10 questions aléatoires depuis la base de données."""
    conn = sqlite3.connect(DB_NAME_QUESTIONS)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 10")
    questions = cursor.fetchall()
    conn.close()
    return questions

# Interface utilisateur avec Streamlit
def main():
    st.title("QCM de Révision - Management et Animation d'Équipe")
    
    # Initialiser les bases de données
    init_dbs()
    
    # Ajouter des questions (exécuter une seule fois si les questions ne sont pas déjà dans la base)
    if st.button("Ajouter des questions (à exécuter si nécessaire)"):
        add_questions_to_db()
    
    # Afficher le meilleur score
    best_name, best_score = get_best_score()
    st.write(f"**Meilleur joueur :** {best_name} avec un score de {best_score}/10")

    # Système de questions
    if st.button("Commencer le QCM"):
        questions = get_random_questions()
        score = 0
        
        # Afficher les questions une par une
        for i, q in enumerate(questions):
            st.write(f"**Question {i + 1}:** {q[1]}")
            user_answer = st.radio("Choisissez votre réponse :", [q[2], q[3], q[4], q[5]], key=i)
            if user_answer == q[6]:
                score += 1
        
        # Résultats
        st.write(f"**Votre score : {score}/10**")
        
        # Enregistrement du score
        name = st.text_input("Entrez votre nom pour enregistrer votre score :")
        if st.button("Enregistrer mon score"):
            if name.strip():
                add_score(name, score)
                st.success("Score enregistré avec succès !")
            else:
                st.error("Veuillez entrer un nom valide.")

if __name__ == "__main__":
    main()
