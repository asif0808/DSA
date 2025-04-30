class User{
    constructor(email,password){
        this.email=email;
        this.password=password        
    }
    //get and set works together i.e. if there is set then there should be get
    get email(){
        return this.Email.toUpperCase()
    }
    set email(value){
          this.Email=value
    }
    get password(){
        return `bcd${this._password}bcd` //showing someone who wants to access
    }
    set password(value){
        this._password=value      //to set/store the value
    }
}
const UserOne=new User("a@gg.com",123)
console.log(UserOne);
console.log(UserOne.password);
console.log(UserOne.email);