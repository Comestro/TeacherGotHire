import React, { useState } from "react";

const ProfileButton = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => setIsOpen(!isOpen);

  return (
    <div className="relative inline-block text-left">
      {/* Button */}
      <button
        onClick={toggleDropdown}
        className="flex items-center px-4 py-2 bg-teal-600 hover:bg-gray-200 rounded-2xl focus:outline-none"
      >
        <img
          src="https://via.placeholder.com/40" // Replace with actual profile image URL
          alt="Profile"
          className="w-8 h-8 rounded-full mr-2"
        />
        <span className="text-sm font-medium">My Profile</span>
      </button>
      {/* Pop-up */}
      <div
        className={`fixed top-0 right-0 h-full w-1/4 bg-gray-100  text-black shadow-lg transform transition-transform ${
          isOpen ? "translate-x-0" : "translate-x-full"
        }`}
      >
        <div className="flex justify-between items-center p-4 border-b">
          <h2 className="text-lg font-bold">Profile</h2>
          <button
            onClick={() => setIsOpen(false)}
            className="text-red-500 hover:text-red-700"
          >
            Close
          </button>
        </div>
        <div className="p-4">
          <p>This is your profile information!</p>
        </div>
      </div>

    </div>
  );
};

export default ProfileButton;
