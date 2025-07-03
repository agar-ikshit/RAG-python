"use client";

import { useState } from "react";
import Link from "next/link";

export default function Sidebar() {
  const [search, setSearch] = useState("");

  const products = [
    { name: "Job Board Software", url: "https://www.logicspice.com/job-board-software" },
    { name: "Fiverr Clone Script", url: "https://www.logicspice.com/fiverr-clone" },
    { name: "Crowdfunding Script", url: "https://www.logicspice.com/crowdfunding-script" },
    { name: "Inventory Management Software", url: "https://www.logicspice.com/inventory-management-software" },
    { name: "Doctor Appointment Scheduling Software", url: "https://www.logicspice.com/doctor-appointment-scheduling-software" },
  
    { name: "Classified Ads Script", url: "https://www.logicspice.com/classified-ads-script" },
   
    {name: "Groupon Clone", url:"https://www.logicspice.com/groupon-clone"},
    {name: "Application Tracking System", url: "https://www.logicspice.com/applicant-tracking-system"},
    {name: "Freelancer Clone", url: "https://www.logicspice.com/freelancer-clone"},
    {name: "LS Inventorizerr", url: "https://www.logicspice.com/inventory-management-software"},
    {name: "Event Booking Software", url: "https://www.logicspice.com/event-booking-software"},
    {name: "Real Estate Script", url: "https://www.logicspice.com/real-estate-script"},
    {name: "Human Resource Management Software", url: "https://www.logicspice.com/hrms-software"},
    {name: "Equipment Rental Script", url: "https://www.logicspice.com/equipment-rental-software"}
  
  ];

  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="w-64 bg-gray-100 p-4 h-screen fixed left-0 top-16 overflow-y-auto">
      <h3 className="text-lg font-semibold mb-4 text-[#EE3953]">
        Logicspice Software Products
      </h3>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search products..."
        className="w-full p-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-[#EE3953]"
      />
      <ul className="space-y-2">
        {filteredProducts.length > 0 ? (
          filteredProducts.map((product, index) => (
            <li key={index} className="text-sm text-gray-700 hover:bg-gray-200 p-2 rounded">
              <Link href={product.url} className="block w-full">
                {product.name}
              </Link>
            </li>
          ))
        ) : (
          <li className="text-sm text-gray-500">No products found</li>
        )}
      </ul>
    </div>
  );
}