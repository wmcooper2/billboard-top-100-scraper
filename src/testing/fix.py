"""Trying to fix todo and finished set"""

def scrape_setup(prev_fin, cur_err, cur_fin):
    """Determines which links need to be scraped. 
        needs;
            - previous stage finished file
            - current stage error file
            - current stage finished file
        Returns 2 Lists."""
    todo = list(set(load_file_list(prev_fin)))
    finished = load_file_list(cur_fin)
#    [todo.remove(el) for el in finished]
    for el in finished:
        try:
            todo.remove(el)
        except:
            pass
    return todo, finished

prev    = "prev.txt"
cur_err = "cur_err.txt"
cur_fin = "cur_fin.txt"

todo, finished  = scrape_setup(prev, cur_err, cur_fin)
todo_len        = len(todo)
fin_len         = len(finished)

print("todo:    ", todo_len)
print("finished:", fin_len)

