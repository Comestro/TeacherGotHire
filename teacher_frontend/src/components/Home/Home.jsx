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
            { label: "SignIn", href: "/login" },
            { label: "Contact US", href: "/contactus" },
            { label: "AboutUs", href: "/about" },
          ]}
          variant="dark"
        />
      </nav>
      <div className="hero h-screen w-full flex items-center justify-center">
        <div className="flex flex-col w-[65%] text-gray-800 mb-10 ">
          <p className="mb-8 font-bold text-6xl leading-none">
            PTPI – Connect with top teachers and great teaching jobs.
          </p>
          <div className="flex items-center rounded-full w-[80%] shadow-lg border-2 mx-20 p-2">
            <input
              type="text"
              placeholder="What subject do you need help with?"
              className="flex-1 p-2 px- border-none focus:outline-none text-gray-600 placeholder-gray-400"
            />
            <div className="h-6 w-px bg-gray-300 mx-4"></div>
            <IoLocationOutline className="text-gray-600" />
            <input
              type="text"
              placeholder="Zip code"
              className="w-28 p-3 border-none focus:outline-none text-gray-600 placeholder-gray-400"
            />
            <button className="bg-blue-600 hover:bg-blue-500 p-2 rounded-full flex items-center justify-center">
              <IoSearchOutline className="text-white w-7 h-7 p-1 " />
            </button>
          </div>

          <div className="mt-4 flex gap-4 mx-20">
            <Button
              textColor="text-teal-700"
              bgcolor="bg-teal-100"
              className="rounded-full opacity-3"
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
  );
}

export default Home;
