print("TO-DO List")
l=[]
n=10

while True:
    
    print("1.To delete,enter 1")
    print("2.To add,enter 2")
    print("3.To exit,enter 3")
    
    choice = int(input("Enter your choice :"))
    
    if choice==1:
        if l:
            item_to_delete =input("Enter an element to delete:")
            if item_to_delete in l:
                l.remove(item_to_delete)
                print("Deleted:",item_to_delete)
                print("Updated List:",l)
            
            else:
                print("Element not found in the list!")
            
        else:
            print("List is empty.Nothing to delete")
    elif choice == 2:
        item_to_add = input("Enter the element to add:")
        l.append(item_to_add)
        print("Added:",item_to_add)
        print("Updated list:",l)
        
    elif choice == 3:
        print("ThankYou!")
        break
    else:
        print("INVALID INPUT")
        