var express = require('express')
var app=express()
var session = require('express-session');
app.use(session({secret:"something"}));
var fs= require('fs');
var body=require('body-parser')
var enc=body({extended:false});
var mysql=require('mysql')
var path=require('path')
app.listen(8000)
app.use(express.static('public'));
mysq=mysql.createConnection({host:"localhost", user:"palani", password:"password", database:"blog"});
mysq.connect();

app.get('/', function(req,res){

  console.log("route section");
  res.sendFile(path.join(__dirname+'/public/login.html'));
    

});


//login authentication

 app.post('/login', enc, function(req,res) {
             sql="select username,email_id from user where username=? and password=?";
             Params=[req.body.username, req.body.password]
             mysq.query(sql,Params,function(error,user) {
                 mysq.end();
                 if(error) console.log(error);
                 else{
                  console.log(user[0].username);
                  req.session.username=user[0].username;
                  req.session.email_id=user[0].email_id;
                  req.session.user=user;
                  res.sendFile(path.join(__dirname+'/public/dashboard.html'));
                  
               }});
});


//usercreation

app.post('/usercreation', enc, function(req,res) {
          if(req.session.user) {
           sql ='insert into user values(username,password,email_id) (?,?,?)';
           Params=[req.body.username,req.body.password,req.body.email_id];
             mysq.query(sql,Params,function(error,result) {
                 mysq.end();
                 if(error) console.log(error);
                 else{
                  msg="User created successfully";
                  console.log(msg);
                  res.json(200,msg);

               }});


}

else {

  res.redirect('/');

}

});


//File creation

app.post('/fswrite', function(req,res) {
      fs.writeFile(req.body.filename, req.body.file, 'binary', function(err,success) {

       if(err) console.log(err);
       else{
          console.log("file created");

          res.json(200, "filecreated");
    }});

});

//readFile

app.get('/fsread', function(req,res) {

         fs.readFile(req.filename, function(err,success) {

             if(err) console.log(err);
             else{
                 res.json(200, success);

              }});
               });



//logout

app.get('/logout', function(req, res) {
      req.session.destroy();
      console.log("FRom the logout section");
      return res.json(200, "Logout Successfully");
    });
