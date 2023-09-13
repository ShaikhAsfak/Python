# The list is a sequence data type which is used to store the collection of data.
qlist = [] # qlist is created to store Data.

print("*************************")
print("****Quiz Application****")
print("*************************")

print('''\nSelect Your Choice:
1. Attempt Quiz
2. Add Question
3. Exit''')

ch = 0

while(ch != 3):
	ch=int(input("\nEnter Your Choice : "))
	
	if ch == 1:
		if(len(qlist) == 0):
			print("No Question is to be Attempted , Please add question")
		else:
			rans=0	#Right Answer
			wans=0	#Wrong Answer
			print("\n***Attempt Quiz Now***\n")

			for q in qlist:
				print("Que : " , q['qt'])
				print("(A) : " , q['A'])
				print("(B) : " , q['B'])
				print("(C) : " , q['C'])
				print("(D) : " , q['D'])
				print("\n NOTE : Enter A , B , C , D Only\n")
				ans = input("Answer : ")

				if q['CAns'] == ans:	#Comparing given answer with correct answer.
					rans=rans+1
				else:
					wans=wans+1

			print("\nTotal Question Attempt : " , rans+wans)
			print("Total Correct Answer : " , rans)
			print("Total Wrong Answer : " , wans , "\n")

	if ch == 2:
		print("\nAdd New Question Here:\n")

		"""Dictionary in Python is a collection of keys values, used to store data values like a map, 
		which, unlike other data types which hold only a single value as an element."""
		
		q = {} #q dictionary is created to store Question and Answer in Key-Value pair.

		q['qt'] = input("Enter Question : ")
		q['A'] = input("Option A = ")
		q['B'] = input("Option B = ")
		q['C'] = input("Option C = ")
		q['D'] = input("Option D = ")
		q['CAns'] = input("Enter Correct Option (A, B, C, D) : ")

		qlist.append(q)	#Storing q (Dictionary) in qlist(List).
		print("\nQuestion has Added Successfully\n")
		