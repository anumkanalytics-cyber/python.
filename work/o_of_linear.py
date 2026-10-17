def find_paper(papers, names):
        for paper in papers:
          if paper == names:
            return True 
        return False

papers = ["ali", "amna", "muhammad", "ifra", "sara", "zara", "Momna", "Mustafa"]

search_name = "sara"

result = find_paper(papers, search_name)

if result:
    print("paper found")
else:
    print("paper not found")
