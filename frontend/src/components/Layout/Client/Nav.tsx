import { HeaderLink } from "./HeaderLink";

export function Nav() {
  return (
    <div
      className="absolute flex justify-between items-center mt-[20px] mx-0 my-auto w-[70vw] px-[100px] h-[60px] bg-indigo-300 rounded-[20px] shadow-indigo-500 shadow-lg
          bg-[url(https://images.pexels.com/photos/20574181/pexels-photo-20574181.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)]
        "
    >
      <div className="flex gap-2">
        <HeaderLink to={`/`}>Home</HeaderLink>
        <HeaderLink to={`/news`}>News</HeaderLink>
        <HeaderLink to={`/blog`}>Blog</HeaderLink>
        <HeaderLink to={`/about`}>About</HeaderLink>
      </div>
      <div>
        <HeaderLink to={`/admin/login`}>Login</HeaderLink>
      </div>
    </div>
  );
}
