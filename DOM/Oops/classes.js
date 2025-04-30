class User{
    constructor(username,email,password){
         this.username=username
         this.email=email
         this.password=password
    }
    encryptPassword(){
        return `abc${this.password}cba`
    }
    UpperCaseName()
    {
        return this.username.toUpperCase()
    }
}
const UserOne=new User('aasif','aasif@gg.com',123)
const UserTwo=new User('john','john@gmail.com',432)
console.log(UserOne.encryptPassword())
console.log(UserOne.username);
console.log(UserTwo.username);
console.log(UserOne.UpperCaseName());
// behind the scene (using function only)
function FUser(username,email,password) {
    this.username=username
    this.email=email
    this.password=password
}
FUser.prototype.encryptPassword=function () {
    return `abc${this.password}cba`
}
FUser.prototype.UpperCaseName=function () {
    return `${this.username.toUpperCase()}`
}
const FUserOne=new FUser('fone','ff@gg.com',6543)
console.log(FUserOne);
console.log(FUserOne.encryptPassword());
console.log(FUserOne.UpperCaseName());
