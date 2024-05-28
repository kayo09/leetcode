**Student Attendance Record II**
_________________________

Attendance->
    &ensp; -String made of character, each character signifies whether the **Student** was **Absent(A)**,**Late(L)** or **Present(P)**

Attendance Award->
    -&ensp; if **both** criterias are met:
        &ensp; &ensp; i.The student was **A** for strictly fewer than 2 days total 
        &ensp; &ensp;ii.The Student was never **L** for 3 or more consecutive days 

To do: 
    &ensp;-Given int n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large therefore, $$n\%(10^9+7)$$ 