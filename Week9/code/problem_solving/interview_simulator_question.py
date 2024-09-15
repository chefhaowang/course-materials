def ask_questions(questions):
    """
    This function asks each interview question and collects the user's response.
    
    Args:
    questions (list): A list of interview questions to ask the user.
    
    Returns:
    list: A list of the user's responses.
    """
    pass


def evaluate_clarity(response):
    """
    This function evaluates the clarity of a response based on its length.
    
    Args:
    response (str): The user's response to a question.
    
    Returns:
    tuple: A score (1-10) and feedback string.
    """
    pass


def evaluate_confidence(response):
    """
    This function evaluates the confidence level of a response based on specific keywords.
    
    Args:
    response (str): The user's response to a question.
    
    Returns:
    tuple: A score (1-10) and feedback string.
    """
    uncertain_words = ["I think", "maybe", "I'm not sure", "possibly"]

    strong_action_verbs = ["I developed", "I managed",
                           "I led", "I improved", "I designed"]

    pass


def evaluate_conciseness(response):
    """
    This function evaluates the conciseness of a response based on its length.
    
    Args:
    response (str): The user's response to a question.
    
    Returns:
    tuple: A score (1-10) and feedback string.
    """
    pass


def provide_feedback(questions, responses):
    """
    This function provides feedback based on the user's responses to each question.
    It evaluates clarity, confidence, and conciseness and prints detailed feedback.
    
    Args:
    questions (list): A list of questions asked in the interview round.
    responses (list): A list of user responses to the questions.
    """
    pass


def run_interview_simulator():
    """
    This function simulates the interview process with multiple rounds.
    Each round consists of different types of questions (introduction, technical, behavioral).
    The user's responses are evaluated, and feedback is provided for each round.
    """
    rounds = {
        "Introduction Round": [
            "Tell me about yourself.",
            "Why did you choose this field?",
            "What motivates you?"
        ],
        "Technical Round": [
            "Explain a challenging technical project you've worked on.",
            "How do you troubleshoot problems in your code?",
            "Describe a technical skill you're currently improving."
        ],
        "Behavioral Round": [
            "Tell me about a time you handled conflict at work.",
            "How do you handle tight deadlines?",
            "Describe a situation where you led a team."
        ]
    }

    pass


if __name__ == "__main__":
    run_interview_simulator()
