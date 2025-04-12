import heapq
from collections import defaultdict

class MobilePhone:
    def __init__(self, name, price, review_score):
        self.name = name
        self.price = price
        self.review_score = review_score
        self.final_score = 0  # To hold the final score for ranking

    def __lt__(self, other):
        # Comparison based on final score for the heap
        return self.final_score > other.final_score  # Higher score is better

class MobileRecommendation:
    def __init__(self):
        self.phones = []
        self.graph = defaultdict(list)

    def load_phones(self, filename):
        with open(filename, 'r') as file:
            for line in file.readlines()[1:]:  # Skip header
                name, price, review_score = line.strip().split(';')
                phone = MobilePhone(name, int(price), float(review_score))
                self.phones.append(phone)

        self.build_graph()

    def build_graph(self):
        for i in range(len(self.phones)):
            for j in range(i + 1, len(self.phones)):
                if abs(self.phones[i].review_score - self.phones[j].review_score) < 0.5:
                    self.graph[self.phones[i]].append(self.phones[j])
                    self.graph[self.phones[j]].append(self.phones[i])

    def normalize_and_score(self):
        # Find min and max values for normalization
        min_price = min(phone.price for phone in self.phones)
        max_price = max(phone.price for phone in self.phones)
        min_review = min(phone.review_score for phone in self.phones)
        max_review = max(phone.review_score for phone in self.phones)

        # Calculate scores for each phone
        for phone in self.phones:
            normalized_review = (phone.review_score - min_review) / (max_review - min_review)
            normalized_price = (max_price - phone.price) / (max_price - min_price)
            # You can adjust weights as needed
            phone.final_score = 0.7 * normalized_review + 0.3 * normalized_price

    def recommend_phones(self, search_name):
        # First normalize and calculate scores for all phones
        self.normalize_and_score()

        # Create a min-heap based on final score
        min_heap = []
        
        # Search for matching phones and push onto the heap
        for phone in self.phones:
            if search_name.lower() in phone.name.lower():
                heapq.heappush(min_heap, phone)

        # Retrieve top 5 recommendations from the heap
        recommendations = []
        while min_heap and len(recommendations) < 5:
            recommendations.append(heapq.heappop(min_heap))

        # Collect additional recommendations from the graph based on initial matches
        additional_recommendations = set()
        for phone in recommendations:
            for neighbor in self.graph[phone]:
                if neighbor not in recommendations:
                    additional_recommendations.add(neighbor)

        # Combine recommendations with additional ones, ensuring uniqueness
        for neighbor in additional_recommendations:
            if len(recommendations) < 5 and neighbor not in recommendations:
                recommendations.append(neighbor)

        # Sort the final recommendations again based on final score if needed
        recommendations.sort(key=lambda x: x.final_score, reverse=True)

        return recommendations

def main():
    recommendation_system = MobileRecommendation()
    recommendation_system.load_phones('mobile_phones.txt')

    search_name = input("Enter the name of the mobile phone to search: ")
    recommendations = recommendation_system.recommend_phones(search_name)

    if recommendations:
        print("\nRecommended Mobile Phones:")
        for phone in recommendations:
            print(f"Name: {phone.name}, Price: {phone.price}, Review Score: {phone.review_score}, Final Score: {phone.final_score:.2f}")
    else:
        print("No recommendations found.")

if __name__ == "__main__":
    main()