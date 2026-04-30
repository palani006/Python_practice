const studentName = "Rajesh";
const age = 20;
const city = "kuppam";
const isAdult = age >= 18;

function StudentInfo() {
  return (
    <div className="sma-student-card">
      <h2>{studentName}</h2>
      <p>Born in:{2026 - age}</p>
      <span className={isAdult ? "sma-tag-adult" : "sma-tag-minor"}>
        t{isAdult ? "Adult" : "minor"}
      </span>
      <p>Locate:{city + "<Andra Pradesh"}</p>
      <p>profite:{"${studentName},${age}yeasr,${city}"}</p>
      <P>Name length:{studentName.toUpperCase()}</P>
    </div>
  );
}
