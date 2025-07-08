# analyze_scores.py

def analyze_scores():
    with open('scores.txt', 'r') as file:
        scores = file.readlines()
    
    total_score = sum(int(line.split(":")[1]) for line in scores)
    average_score = total_score / len(scores) if scores else 0

    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score}")

if __name__ == '__main__':
    analyze_scores()
