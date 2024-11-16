

import React from "react";
import ProfileButton from "../Profile_Button/Profile_Button";


const Navbar = ({ links, variant, externalComponent: ExternalComponent }) => {
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