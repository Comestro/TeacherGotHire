import React from 'react'
import Navbar  from '../Navbar/Navbar'
import Input from '../Input'
import Button from '../Button'
import { IoSearchOutline } from "react-icons/io5";
import Footer from '../Footer/Footer';
import RoleSelection from '../RoleSelection';
import { useNavigate } from 'react-router-dom';


function Home() {
  
  const navigate = useNavigate();

  const handleRoleSelection = (role) => {
    navigate(`/signup/${role}`);
  };
  
  return (
    <div>
      <nav>
        <Navbar
            links={[
              { label: "SignIn", href: "/login" },
              { label: "Contact US", href: "/contactus" },
              { label: "AboutUs", href: "/about" },
            ]}
            variant="dark"
        />
      </nav>
      <div className='hero w-full mt-40 flex justify-center relative'>
        
        <div className='flex flex-col w-[45%]'>
        <p className='mb-8 font-semibold text-6xl font-sans'>PTPI – Connect with top teachers and great teaching jobs</p>
        <div className=' relative'>
             <Input
             placeholder='Please enter subject and location'
             className='p-4 rounded-xl w-full shadow-xl border-2 pl-10 '/>
             <IoSearchOutline  className=' absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500'/>
          </div>
          <div className='mt-4 flex gap-4'>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200'className='rounded-2xl opacity-3'>Math</Button>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200' className='rounded-2xl'>English</Button>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200' className='rounded-2xl'>English</Button>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200' className='rounded-2xl'>English</Button>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200' className='rounded-2xl'>English</Button>
            <Button textColor='text-teal-700' bgcolor='bg-teal-200' className='rounded-2xl'>English</Button>
          </div>
        </div>
       </div>
        <RoleSelection onSelectRole={handleRoleSelection}/>
        <Footer/> 
     </div>
    
  )
}

export default Home