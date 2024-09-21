import { Link } from "@tanstack/react-router"

export function BlogItem(props: any) {
  const { data } = props;
  return (
    <div>
      <Link
        className="hover:text-yellow-500"
        to={`/blog/${props.data.id}`}
      >
        <h1 className="flex text-[16px] my-[10px] before:block before:content-['·'] before:text-yellow-600 before:mr-[4px]">
          {data.title}
        </h1>
      </Link>
    </div>
  );
}