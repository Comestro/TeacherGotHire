// import React from 'react'
// import { useForm } from 'react-hook-form'


// function EditableCard() {

//     const navigate = useNavigate();
//     const { register, handleSubmit } = useForm();


//   return (
//     <div>
//           <form onSubmit={handleSubmit(signup)} className="space-y-6">
//                 <Input
//                   label="Full Name"
//                   placeholder="Enter your full name"
//                   {...register('name', { required: true })}
//                 />
//           </form>
//     </div>
//   )
// }

// export default EditableCard

import React, { useState } from "react";

const EditableCard = ({ initialData, onSave }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ ...initialData });

  const handleEditToggle = () => {
    if (isEditing && onSave) {
      onSave(formData); // Call the onSave function with updated data
    }
    setIsEditing(!isEditing); // Toggle the mode
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div className="w-full flex justify-center bg-white shadow-lg rounded-lg p-6">
      {isEditing ? (
        <div>
          {Object.keys(formData).map((key) => (
            <div key={key} className="mb-4">
              <label className="block text-sm font-medium text-gray-700 capitalize">
                {key}
              </label>
              <input
                type="text"
                name={key}
                value={formData[key]}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border rounded-lg"
                placeholder={`Enter ${key}`}
              />
            </div>
          ))}
        </div>
      ) : (
        <div>
          {Object.entries(formData).map(([key, value]) => (
            <div key={key} className="mb-2">
              <span className="block text-sm font-medium text-gray-700 capitalize">
                {key}:
              </span>
              <p className="text-gray-600">{value}</p>
            </div>
          ))}
        </div>
      )}
      <button
        onClick={handleEditToggle}
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-600"
      >
        {isEditing ? "Save" : "Edit"}
      </button>
    </div>
  );
};

export default EditableCard;
