def ask_questions(questions):
    """
    This function asks each interview question and collects the user's response.
    
    Args:
    questions (list): A list of interview questions to ask the user.
    
    Returns:
    list: A list of the user's responses.
    """
    responses = []
    for question in questions:
        print(f"\nQuestion: {question}")  
        response = input("Your response: ")  
        responses.append(response)  
    return responses  


def evaluate_clarity(response):
    """
    This function evaluates the clarity of a response based on its length.
    
    Args:
    response (str): The user's response to a question.
    
    Returns:
    tuple: A score (1-10) and feedback string.
    """
    if len(response) < 20:
        return 4, "Needs improvement (too short)"  # Response is too short
    elif len(response) > 200:
        return 6, "Needs improvement (too lengthy)"  # Response is too long
    else:
        return 9, "Good"  # Response has a good length


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

    for word in uncertain_words:
        if word in response:
            # Low confidence detected
            return 5, "Needs improvement (uncertain language)"

    # Check for strong action verbs
    for verb in strong_action_verbs:
        if verb in response:
            return 9, "Strong"  # High confidence detected

    return 7, "Good"  


def evaluate_conciseness(response):
    """
    This function evaluates the conciseness of a response based on its length.
    
    Args:
    response (str): The user's response to a question.
    
    Returns:
    tuple: A score (1-10) and feedback string.
    """
    if len(response) < 50:
        return 4, "Too short"  # Response is too short
    elif len(response) > 150:
        return 5, "Too detailed"  # Response is too detailed
    elif len(response) > 100 and len(response) < 150:
        return 7, "Good but slightly long"  # Response is good but a bit long
    else:
        return 9, "Excellent"  # Response is well-balanced


def provide_feedback(questions, responses):
    """
    This function provides feedback based on the user's responses to each question.
    It evaluates clarity, confidence, and conciseness and prints detailed feedback.
    
    Args:
    questions (list): A list of questions asked in the interview round.
    responses (list): A list of user responses to the questions.
    """
    total_score = 0  

    for i, response in enumerate(responses):
        print(f"\nQuestion: {questions[i]}") 

        clarity_score, clarity_feedback = evaluate_clarity(response)
        confidence_score, confidence_feedback = evaluate_confidence(response)
        conciseness_score, conciseness_feedback = evaluate_conciseness(
            response)

        total_score += clarity_score + confidence_score + conciseness_score

        print(f"Clarity: {clarity_feedback} (Score: {clarity_score}/10)")
        print(
            f"Confidence: {confidence_feedback} (Score: {confidence_score}/10)")
        print(
            f"Conciseness: {conciseness_feedback} (Score: {conciseness_score}/10)")

    print(
        f"\nTotal Score for this round: {total_score / (3 * len(questions)) * 10:.2f}/10")



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


    for round_name, questions in rounds.items():
        print(f"\n--- {round_name} ---")  
        responses = ask_questions(questions)
        provide_feedback(questions, responses)
        print("\nMoving to the next round...\n")  

    print("Interview Simulation Completed!")


if __name__ == "__main__":
    run_interview_simulator()
