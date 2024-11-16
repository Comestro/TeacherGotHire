import React from "react"
import  { BrowserRouter,Route,Routes } from "react-router-dom"
import Home from './components/Home/Home'
import SignUpPage from "./components/SignUpPage"
import TeacherDashboard from "./components/Dashboard/TeacherDashboard"
import Payment from "./components/Payment"
import ExamPortal from "./components/ExamPortal/ExamPortal"

function App() {
  

  return (
    <>
     <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path="/signup/:role" element={<SignUpPage />} />
          <Route path="/teacherdashbord" element={<TeacherDashboard/>}/>
          <Route path="/payment" element={<Payment/>}/>
          <Route path="/exam-portal" element={<ExamPortal/>}/>
        </Routes>
     </BrowserRouter>
     
      
    </>
  )
}

export default App
