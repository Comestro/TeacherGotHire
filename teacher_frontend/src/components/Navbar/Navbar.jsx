

import React from "react";
import { useState } from "react";
import { IoIosNotifications } from "react-icons/io";



const Navbar = ({ links, variant, externalComponent: ExternalComponent }) => {

  const [showNotifications, setShowNotifications] = useState(false);
  
  const handleNotificationClick = () => {
    setShowNotifications(!showNotifications);
  };
  return (
    <>
     <nav
      className={` ${
        variant === "light" ? "bg-white text-black" : "bg-teal-500 text-white"
      }`}
    >
      <ul className="flex items-center justify-between px-56 py-1">
         <div className="text-lg font-semibold">PTPI</div>
         {links.map((link, index) => (
          <li key={index}>
            <a
              href={link.href}
              className=""
            >
              {link.label}
            </a>
          </li>
        ))}
         <div className="relative">
          <button
            onClick={handleNotificationClick}
            className="flex items-center px-4 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700"
          >
            {/* Notification Icon */}
            <span className="material-icons mr-2"><IoIosNotifications /></span>
            Notifications

            {/* Show green indicator if there are new notifications */}
            {/* {newNotifications.length > 0 && (
              <span className="absolute top-0 right-0 w-3 h-3 bg-green-500 rounded-full"></span>
            )} */}
          </button>
          </div>
         {ExternalComponent && (
          <div className="ml-4">
            <ExternalComponent />
          </div>
        )} 

      </ul>
    </nav>
    </>
   
  );
};

export default Navbar