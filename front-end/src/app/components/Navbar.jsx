import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-[#EE3953] text-white p-4 shadow-md fixed top-0 w-full z-10">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="https://www.logicspice.com" className="text-xl font-bold">
          Logicspice
        </Link>
        <div className="flex gap-6">
          <Link href="https://www.logicspice.com" className="hover:underline">
            Home
          </Link>
          <Link href="https://www.logicspice.com/services" className="hover:underline">
            Services
          </Link>
          <Link href="https://www.logicspice.com/contact" className="hover:underline">
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
}