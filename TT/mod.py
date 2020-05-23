
class LoginControl extends React.Component {
  
  constructer(props){
    super(props);
    this.LoginClick = this.LoginClick.bind(this);
    this.LogoutClick = this.LogoutClick.bind(this);
    this.state = {IsLoggedIn : false};
  }
  
  LoginClick(){
    this.setState({IsLoggedIn : true});
  }
  
  LogoutClick(){
    this.setState({IsLoggedIn:false});
  }
  
  render(){
    return({
      <div>
      if(IsLoggedIn){
      <button onclick = {this.LogoutClick}>
        Login</button>
      }
      else {
            <button onclick = {this.LoginClick}>
        Logout</button>
          }
        </div>
    }
    
  )}
  
  
  
  
  
  
}
           
              
ReactDOM.render(
              <LoginControl />,
              document.getElementById('root')
              
              
              );