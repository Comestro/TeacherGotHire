import React from "react";
import ProfileButton from "../Profile_Button/Profile_Button";
import { Link } from "react-router-dom";
import { useState } from "react";

const Navbar = ({ links, variant, externalComponent: ExternalComponent }) => {

  const [showNotifications, setShowNotifications] = useState(false);
  
  const handleNotificationClick = () => {
    setShowNotifications(!showNotifications);
  };
  return (
    <>
      <nav
        className={`flex items-center justify-between  py-2 px-10 ${
          variant === "light" ? "bg-white text-black" : "bg-white-500 text-black"
        }`}
      >
        <div className="text-3xl font-bold text-gray-950">
            PTPI.COM
        </div>
        <div className="flex items-center justify-between">
          {links.map((link, index) => (
            <a href="#" key={index}>
              <div className="flex gap-4">
              <Link href={link.href} className="font-semibold text-gray-600 px-3 p-2">
                {link.label}
              </Link>
              </div>
            </a>
          ))}
          {ExternalComponent && (
            <div className="ml-4">
              <ExternalComponent />
            </div>
          )}
        </div>
      </nav>
    </>
  );
};

export default Navbar;
