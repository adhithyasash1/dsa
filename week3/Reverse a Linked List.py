def reverse(self):
    previous = None
    current = self
    while current is not None:
        next = current.next
        current.next = previous        
        previous = current
        current = next
    return previous
                        
