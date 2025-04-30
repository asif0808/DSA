class Student{
    constructor(username){
        this.username=username
    }
    logMe(){
        console.log(`Username is ${this.username}`);
        
    }
}
class Teacher extends Student{
    constructor(username,email,password){
        super(username)
        this.email=email
        this.password=password
    }
    addCourse(){
        console.log(`course is added by ${this.username}`);
        
    }
}
const T1=new Teacher('aasif','a@agg.com',432)
console.log(T1);
T1.addCourse()
T1.logMe()
const S1=new Student('UserOne')
S1.logMe()
//S1.addCourse() ==> error as it is not accessible
// instanceOf()
console.log(T1 instanceof Teacher);
console.log(T1 instanceof Student);
console.log(S1 instanceof Student);
console.log(S1 instanceof Teacher);
// console.log(Student instanceof Teacher);
// console.log(Teacher instanceof Student);
