class User{
    constructor(username){
        this.username=username
    }
    logMe(){
        console.log(`Username is ${this.username}`);
    }
    static Id(){  //not accessible
        return `123`
    }
}
const UserOne=new User('aasif')
UserOne.logMe()
// console.log(UserOne.Id());  throws error
class Owner extends User{
    constructor(username,email){
        super(username)
        this.email=email
    }
}
const OwnerOne=new Owner('aasif','a@g.com')
OwnerOne.logMe()
// OwnerOne.Id() ===> throws error
