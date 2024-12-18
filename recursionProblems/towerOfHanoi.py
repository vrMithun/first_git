def fun(n,s,e,a):
    if n==1:
        print(f"move disk 1 form {s} to {e}")
        return
    fun(n-1,s,a,e)
    print(f"move disk {n} from {s} to {e}")
    fun(n-1,a,e,s)
fun(3,'A','B','C')        