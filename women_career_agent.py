# Women Career Agent 👩‍💼
# Helps women with job hunting and career progress

def career_agent(question):
    question = question.lower()

    # CV and Resume Help
    if "cv" in question or "resume" in question:
        return """
        📄 CV TIPS FOR YOU:
        1. Keep your CV to 1-2 pages
        2. Always put your most recent job first
        3. Use strong action words like: built, managed, designed, led
        4. Add your GitHub link if you have projects
        5. Tailor your CV for each job you apply to
        """

    # Interview Help
    elif "interview" in question:
        return """
        🎤 INTERVIEW TIPS:
        1. Research the company before you go
        2. Practice: 'Tell me about yourself' answer
        3. Prepare 3 examples of your past work
        4. Ask questions at the end - shows interest!
        5. Common question: 'What is your biggest strength?'
        
        Want to practice an interview question? Type 'practice interview'
        """

    # Practice Interview
    elif "practice interview" in question:
        return """
        🎯 INTERVIEW PRACTICE:
        Answer this question:
        'Tell me about a time you solved a difficult problem?'
        
        Think about:
        - What was the situation?
        - What did YOU do?
        - What was the result?
        """

    # Job Search Help
    elif "job" in question or "apply" in question or "search" in question:
        return """
        🔍 JOB HUNTING TIPS:
        1. LinkedIn - update your profile today!
        2. GitHub - show your projects
        3. Network - talk to people in your field
        4. Apply to at least 5 jobs per week
        5. Follow up after 1 week if no reply
        
        Best websites to find jobs:
        - linkedin.com
        - indeed.com
        - glassdoor.com
        """

    # Skills Help
    elif "skill" in question or "learn" in question:
        return """
        📚 TOP SKILLS FOR WOMEN IN TECH 2026:
        1. Python - most in demand!
        2. Machine Learning / AI
        3. Cloud (AWS, Azure, Google Cloud)
        4. Data Analysis
        5. Communication skills
        
        Free learning websites:
        - coursera.org
        - kaggle.com
        - freecodecamp.org
        """

    # Salary Help
    elif "salary" in question or "pay" in question or "money" in question:
        return """
        💰 SALARY TIPS:
        1. Always research salary before interview
        2. Do NOT say a number first - let them offer
        3. It is okay to negotiate - always!
        4. Women often undersell themselves - do not!
        5. Check salaries at: glassdoor.com or levels.fyi
        """

    # Motivation
    elif "motivation" in question or "scared" in question or "nervous" in question or "confidence" in question:
        return """
        💪 YOU GOT THIS!
        - Every expert was once a beginner
        - You are already ahead by learning every day
        - Being a woman in tech is your superpower
        - Maria built her first AI agent today!
        - The tech world NEEDS women like you!
        
        Keep going. You are doing amazing! 🌟
        """

    # Progress tracking
    elif "progress" in question or "track" in question or "goal" in question:
        return """
        📈 TRACK YOUR PROGRESS:
        Week 1: Update CV and LinkedIn
        Week 2: Apply to 5 jobs
        Week 3: Practice interviews
        Week 4: Follow up and network
        
        Tip: Write down 1 small goal every morning!
        """

    # Networking
    elif "network" in question or "connect" in question or "linkedin" in question:
        return """
        🤝 NETWORKING TIPS:
        1. Send 3 connection requests per day on LinkedIn
        2. Write a personal message when connecting
        3. Comment on posts in your field
        4. Join women in tech groups online
        5. Attend hackathons like this one! 🎉
        """

    # Help menu
    elif "help" in question or "what can you do" in question:
        return """
        🤖 I CAN HELP YOU WITH:
        - Type 'cv'           → CV and Resume tips
        - Type 'interview'    → Interview preparation
        - Type 'job'          → Job hunting tips
        - Type 'skills'       → What skills to learn
        - Type 'salary'       → Salary negotiation
        - Type 'motivation'   → When you need a boost
        - Type 'progress'     → Track your career goals
        - Type 'network'      → Networking tips
        """

    else:
        return """
        🤔 I did not understand that.
        Type 'help' to see everything I can do for you!
        """


# Run the Agent
print("=========================================")
print("   👩‍💼 WOMEN CAREER AGENT 👩‍💼")
print("   Your personal career assistant!")
print("=========================================")
print("Type 'help' to get started")
print("Type 'quit' to exit")
print("")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Agent: Good luck with your career journey! You are amazing! 🌟")
        break

    response = career_agent(user_input)
    print("Agent:", response)
    print("") 
