import React from "react";
import Navbar from "../Navbar/Navbar";
import Input from "../Input";
import Button from "../Button";
import { IoSearchOutline } from "react-icons/io5";
import Footer from "../Footer/Footer";
import RoleSelection from "../RoleSelection";
import { useNavigate } from "react-router-dom";
import { IoLocationOutline } from "react-icons/io5";

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
            {id:'1', label: "SignIn", to: "/login" },
            {id:'2', label: "Contact US", to: "/contact" },
            {id:"3", label: "AboutUs", to: "/about" },
          ]}
          variant="dark"
        />
      </nav>
      <div className="hero h-screen w-full flex items-center justify-center">
        <div className="flex flex-col w-[65%] text-gray-800 mb-10 ">
          <p className="mb-8 font-bold text-6xl leading-none">
            PTPI – Connect with top teachers and great teaching jobs.
          </p>
          <div className=" relative">
            <Input
              placeholder="Please enter subject and location"
              className="p-4 rounded-xl w-full shadow-xl border-2 pl-10 "
            />
            <IoSearchOutline className=" absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500" />
          </div>
          <div className="mt-4 flex gap-4">
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl opacity-3"
            >
              Math
            </Button>
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl"
            >
              English
            </Button>
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl"
            >
              English
            </Button>
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl"
            >
              English
            </Button>
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl"
            >
              English
            </Button>
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-2xl"
            >
              English
            </Button>
          </div>
        </div>
      </div>
      <RoleSelection onSelectRole={handleRoleSelection} />
      <Footer />
    </div>
    <div className="flex flex-col gap-2 w-full lg:w-[65%] px-14">
      <div className="flex items-center rounded-full border-2 p-2 bg-white mr-4">
        <input
          type="text"
          placeholder="What subject do you need help with?"
          className="flex-1 p-2 px-2 border-none focus:outline-none text-gray-600  placeholder-gray-400 placeholder:font-semibold placeholder:px-4"
        />
        <div className="h-6 w-px bg-gray-300 mx-4 hidden sm:block"></div>
        <IoLocationOutline className="text-gray-600 hidden sm:block" />
        <input
          type="text"
          placeholder="Pin code"
          className="hidden sm:block w-20 md:w-28 p-3 border-none focus:outline-none text-gray-600 placeholder-gray-400"
        />
        <button className="bg-teal-700 hover:bg-blue-500 p-2 rounded-full flex items-center justify-center">
          <IoSearchOutline className="text-white w-5 h-5 md:w-7 md:h-7 p-1" />
        </button>
      </div>

      <div className="mt-4 flex flex-nowrap gap-4 justify-center">
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-full"
        >
          Math
        </Button>
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-2xl"
        >
          English
        </Button>
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-2xl"
        >
          Science
        </Button>
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-2xl"
        >
          History
        </Button>
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-2xl"
        >
          Geography
        </Button>
        <Button
          textColor="text-teal-700 font-medium"
          bgcolor="bg-teal-100"
          className="rounded-2xl"
        >
          Music
        </Button>
      </div>
    </div>
  </div>
  <RoleSelection onSelectRole={handleRoleSelection} />
  <Footer />
</div>

  );
}

export default Home;
