// object literal
const obj1={
    username:'aasif',
    Emp_no:43,
    greet:function () {
        console.log(`Hello ${this.username}`);
        
        console.log(this);
    }
}
console.log(obj1);
console.log(obj1.username);
obj1.greet();
// console.log(obj1.this); //undefined
console.log(this); //empty object

//importance of new 
function User(name,password,isLogged) {
    this.name=name
    this.password=password
    this.isLogged=isLogged
    this.greeting=function () {
        console.log(`welcome ${this.name}`);
    }
    return this //works same without this line, but recommended to write to increase code readability
}
// creating instances
const UserOne=new User('aasif',342,true)
console.log(UserOne);
const UserTwo=new User('john',253,false)
console.log(UserTwo);
UserOne.greeting()
UserTwo.greeting()


