"use client";

import { useState } from "react";

export default function Sidebar() {
  const [search, setSearch] = useState("");

  const products = [
    "Job Board Software",
    "Fiverr Clone Script",
    "Crow funding Script",
    "Inventory Management Software",
    "Doctor Appointment Scheduling Software",
    "Hotel Management Software",
    "Order Management Software",
    "Classified Ads Script",
    "Group Chat Internal Communication Software",
    "Recruitment Management Software",
    "PHP Review Script",
    "FAQ Script",
  ];

  const filteredProducts = products.filter((product) =>
    product.toLowerCase().includes(search.toLowerCase())
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
              {product}
            </li>
          ))
        ) : (
          <li className="text-sm text-gray-500">No products found</li>
        )}
      </ul>
    </div>
  );
}