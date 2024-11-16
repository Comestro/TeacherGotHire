import React from 'react'
import Navbar from '../Navbar/Navbar'
import { useNavigate } from 'react-router-dom';
import ProfileButton from '../Profile_Button/Profile_Button';

function TeacherDashboard() {

    const navigate = useNavigate();

    const handleExamStart = () => {
      navigate('/payment'); // Redirect to payment page
    };

  return (
    <div>
      <nav className=''>
        <div className=''>
          <Navbar
              links={[
                  { label: "Contact US", href: "/contactus" },
                  { label: "AboutUs", href: "/about" },
                ]}
                variant="dark"
                externalComponent={ProfileButton}
              />
        </div>
       </nav>
         <div className="max-w-4xl mx-auto p-6 bg-gray-100 rounded-lg shadow-lg">
      <h1 className="text-3xl font-bold text-blue-600 text-center mb-4">
        Become a Certified Tutor!
      </h1>
      <p className="text-lg text-gray-700 mb-4">
        Join our network of professional tutors by completing a simple exam. Here's how the process works:
      </p>
      <ul className="list-disc pl-5 text-gray-600 mb-6">
        <li className="mb-2">Pay a minimal registration fee to enroll for the exam.</li>
        <li className="mb-2">Take the exam to demonstrate your teaching skills.</li>
        <li>Start your journey as a certified tutor with us!</li>
      </ul>
      <p className="text-lg font-medium text-gray-800 mb-6">
        Registration Fee: <span className="text-green-600 font-bold">₹500</span>
      </p>
      <div className="text-center">
        <button
          onClick={handleExamStart}
          className="px-6 py-3 bg-blue-500 text-white font-bold rounded-lg shadow hover:bg-blue-600 transition"
        >
          Proceed to Exam
        </button>
      </div>
    </div>  
    </div>
  )
}

export default TeacherDashboard