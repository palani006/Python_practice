const isLoggedIn = true;
const hasError = false;
const errorMessage = "Network error";
function Example() {
  <div className="sma-status-box">
    {hasError && <p className="sma-error">{errorMessage}</p>}
    {isLoggedIn ? (
      <p className="sma-welcome">Welcome Back!</p>
    ) : (
      <p className="sam-login-prompt">please log in</p>
    )}
    {hasError ? <p className="sma-error">{errorMessage}</p> : null}
  </div>;
}
export default Example;
