function setUserName(username) {
    this.username=username
    console.log('called');
    
}
function CreateUser(username,email,password) {
      setUserName.call(this,username) //call hold this of called function
      this.email=email;
      this.password=password    
}
const UserOne=new CreateUser('aasif','a@a.com',333)
console.log(UserOne);
